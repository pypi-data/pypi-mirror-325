import io
import json
import threading
import time
import requests
import logging

DEFAULT_REQUESTS_PER_MINUTE_LIMIT = 900
logger = logging.getLogger(__name__)


class IrysException(Exception):
    pass


class IrysNetworkException(IrysException):
    pass


class HTTPClient:
    def __init__(
        self,
        api_url,
        timeout=None,
        retries=10,
        outgoing_connections=256,
        requests_per_period=DEFAULT_REQUESTS_PER_MINUTE_LIMIT,
        period_sec=60,
        extra_headers={},
        cert_fingerprint=None,
    ):
        self.api_url = api_url
        self.session = requests.Session()
        self.max_outgoing_connections = outgoing_connections
        self.outgoing_connection_semaphore = threading.BoundedSemaphore(
            outgoing_connections
        )
        self.rate_limit_lock = threading.Lock()
        self.requests_per_period = requests_per_period
        self.ratelimited_requests = 0
        self.period_sec = period_sec
        # self.incoming_port = incoming_port
        self.extra_headers = extra_headers
        self.req_history = []
        max_retries = requests.adapters.Retry(
            total=retries, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504]
        )  # from so
        https_adapter = self._FingerprintAdapter(
            fingerprint=cert_fingerprint,
            pool_connections=outgoing_connections,
            pool_maxsize=outgoing_connections,
            max_retries=max_retries,
            pool_block=True,
        )

        http_adapter = requests.adapters.HTTPAdapter(
            pool_connections=outgoing_connections,
            pool_maxsize=outgoing_connections,
            max_retries=max_retries,
            pool_block=True,
        )
        self.session.mount("http://", http_adapter)
        self.session.mount("https://", https_adapter)

        self.timeout = timeout

    def __del__(self):
        self.session.close()

    class _FingerprintAdapter(requests.adapters.HTTPAdapter):
        def __init__(self, fingerprint=None, **kwparams):
            self.fingerprint = fingerprint
            super().__init__(**kwparams)

        def init_poolmanager(self, connections, maxsize, block=False):
            self.poolmanager = requests.packages.urllib3.poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                assert_fingerprint=self.fingerprint,
            )

    def ratelimited(self):
        if self.requests_per_period is None:
            return False
        with self.rate_limit_lock:
            now = time.time()
            queued_requests = 0
            for idx, then in enumerate(self.req_history):
                if then + self.period_sec >= now:
                    queued_requests_idx = idx
                    queued_requests = len(
                        self.req_history) - queued_requests_idx
                    break
            return (
                queued_requests + self.ratelimited_requests >= self.requests_per_period
            )

    def ratelimit_suggested(self):
        if self.requests_per_period is None:
            return False
        if len(self.req_history) == 0:
            return False
        return (
            time.time() - self.req_history[-1]
            < self.requests_per_period / self.period_sec
        ) or self.ratelimited

    def _ratelimit_prologue(self):
        if self.requests_per_period is None:
            return
        with self.rate_limit_lock:
            now = time.time()
            queued_requests = 0
            # if len(self.req_history) >= 3600:
            #    import pdb; pdb.set_trace()
            for idx, then in enumerate(self.req_history):
                if then + self.period_sec >= now:
                    queued_requests_idx = idx
                    queued_requests = len(
                        self.req_history) - queued_requests_idx
                    break
            if queued_requests + self.ratelimited_requests < self.requests_per_period:
                # if len(self.req_history) >= self.requests_per_period:
                #    import pdb; pdb.set_trace()
                self.req_history.append(now)
                return
        # print(f'{self.api_url}: too many requests in prologue')
        self.on_too_many_requests()
        with self.rate_limit_lock:
            now = time.time()
            if len(self.req_history) >= self.requests_per_period:
                duration = (
                    self.req_history[-self.requests_per_period + 1]
                    + self.period_sec
                    - now
                )
                if duration > 0:
                    if duration > 0.5:
                        # quick workaround to let this display later during lock contention
                        time.sleep(0.5)
                        duration -= 0.5
                    logger.info(
                        f"Sleeping for {int(duration*100)/100}s to respect ratelimit of {
                            self.requests_per_period}req/{self.period_sec}s ..."
                    )
                    time.sleep(duration)
                    # import pdb; pdb.set_trace()
                    logger.info(
                        f"Done sleeping for {int(duration*100)/100}s to respect ratelimit of {
                            self.requests_per_period}req/{self.period_sec}s ."
                    )
        return self._ratelimit_prologue()

    def _ratelimit_epilogue(self, success=True):
        if self.requests_per_period is None:
            return
        if success:
            with self.rate_limit_lock:
                self.ratelimited_requests = 0
                now = time.time()
                for req_idx, req_time in enumerate(self.req_history):
                    if req_time + self.period_sec > now:
                        self.req_history = self.req_history[req_idx:]
                        break
        else:
            with self.rate_limit_lock:
                self.ratelimited_requests += 1
                now = time.time()
                # import pdb; pdb.set_trace()
                if len(self.req_history):
                    self.period_sec = max(
                        self.period_sec, now - self.req_history[0])
                if (
                    len(self.req_history) - self.ratelimited_requests
                    <= self.requests_per_period
                ):
                    self.requests_per_period = max(
                        1, len(self.req_history) - self.ratelimited_requests
                    )
                logger.info(
                    f"Rate limit hit. Dropped rate to {
                        self.requests_per_period}/{self.period_sec}s."
                )
            self.on_too_many_requests()

    # _get and _post should just call a _request function to share code
    def _request(self, *params, **request_kwparams):
        if len(params) and params[-1][0] == "?":
            url = self.api_url + "/" + "/".join(params[:-1]) + params[1]
        else:
            url = self.api_url + "/" + "/".join(params)

        headers = {**self.extra_headers, **request_kwparams.get("headers", {})}
        request_kwparams["headers"] = headers

        while True:
            self._ratelimit_prologue()
            response = None
            try:
                if not self.outgoing_connection_semaphore.acquire(blocking=False):
                    self.on_too_many_connections()
                    logger.info(
                        "Waiting for connection count limit semaphore to drain..."
                    )
                    self.outgoing_connection_semaphore.acquire()
                try:
                    response = self.session.request(
                        **{"url": url, "timeout": self.timeout, **request_kwparams}
                    )
                finally:
                    self.outgoing_connection_semaphore.release()

                if response.status_code == 400:
                    try:
                        msg = response.json()["error"]
                    except:
                        msg = response.text
                    raise IrysException(msg)

                response.raise_for_status()
                if int(response.headers.get("content-length", 1)) == 0:
                    raise IrysException(f"Empty response from {url}")
                self._ratelimit_epilogue(True)
                return response
            except requests.exceptions.RequestException as exc:
                text = "" if response is None else response.text
                status_code = 0 if response is None else response.status_code
                if status_code == 429:
                    # too many requests
                    self._ratelimit_epilogue(False)
                    self.on_too_many_requests()
                    continue
                if (
                    type(exc) is requests.ConnectionError
                    and len(exc.args) > 0
                    and type(exc.args[0]) is requests.urllib3.exceptions.ClosedPoolError
                ):
                    # strange ClosedPoolError from urllib3 race condition? https://github.com/urllib3/urllib3/issues/951
                    self._ratelimit_epilogue(False)  # to reduce busylooping
                    continue
                if type(exc) is requests.ReadTimeout:
                    if status_code == 0:
                        status_code = 598
                    logger.info("{}\n{}\n\n{}".format(
                        exc, text, request_kwparams))
                else:
                    pass
                if status_code == 520:
                    # cloudfront broke
                    self._ratelimit_epilogue(True)
                    continue
                elif status_code == 502:
                    # cloudflare broke
                    self._ratelimit_epilogue(True)
                    continue
                self.on_network_exception(text, status_code, exc, response)
                raise IrysNetworkException(
                    text or repr(type(exc)), status_code, exc, response
                )
            except:
                self._ratelimit_epilogue(True)
                raise

    def _get(self, *params, **request_kwparams):
        return self._request(*params, **{"method": "GET", **request_kwparams})

    def _get_json(self, *params, **request_kwparams):
        response = self._get(*params, **request_kwparams)
        try:
            return response.json()
        except:
            raise IrysException(response.text)

    def _post(self, data, *params, headers={}, **request_kwparams):
        headers = {**headers}

        if type(data) is dict:
            headers.setdefault("Content-Type", "application/json")
            data_key = "json"
        else:
            if isinstance(data, (bytes, bytearray)):
                headers.setdefault("Content-Type", "application/octet-stream")
            else:
                headers.setdefault("Content-Type", "text/plain")
            data_key = "data"

        return self._request(
            *params,
            **{
                "method": "POST",
                "headers": headers,
                **{data_key: data},
                **request_kwparams,
            },
        )

    def _post_json(self, data, *params, **request_kwparams):
        response = self._post(data, *params, **request_kwparams)
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            raise IrysException(response.text)

    def on_network_exception(self, text, code, exception, response):
        text = f"{self.api_url} - {text}"
        raise IrysNetworkException(text, code, exception, response)

    def on_too_many_connections(self):
        pass

    def on_too_many_requests(self):
        return self.on_too_many_connections()
