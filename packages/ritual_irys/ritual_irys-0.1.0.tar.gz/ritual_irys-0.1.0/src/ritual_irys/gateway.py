from ritual_irys.http import HTTPClient
from ritual_irys.utils import DEFAULT_GATEWAY
DEFAULT_REQUESTS_PER_MINUTE_LIMIT = 900


class Node(HTTPClient):

    def __init__(
        self,
        api_url=DEFAULT_GATEWAY,
        timeout=None,
        retries=5,
        outgoing_connections=DEFAULT_REQUESTS_PER_MINUTE_LIMIT,
        requests_per_period=DEFAULT_REQUESTS_PER_MINUTE_LIMIT,
        period_sec=60,
        incoming_port=None,
    ):
        super().__init__(
            api_url,
            timeout,
            retries,
            outgoing_connections,
            requests_per_period,
            period_sec,
            extra_headers={"X-P2p-Port": str(incoming_port)}
            if incoming_port is not None
            else {},
        )

    def tx_field(self, hash, field):
        """
        Return a given field of the transaction specified by the transaction ID (hash).

        {field} := {
            'id' | 'last_tx' | 'owner' | 'tags' | 'target' | 'quantity' |
            'data_root' | 'data_size' | 'data' | 'reward' | 'signature'
        }
        """
        match field:
            case "data":
                response = self._get("tx", hash, "data")
                return response.content
            # case "data_size":
            #     response = self._get_json("tx", hash)
            #     return response["data_size"]
            case _:
                response = self._get_json("tx", hash)
                # for tag in response:
                #     for key in tag:
                #         tag[key] = b64dec(tag[key].encode())
                return response[field]

    def tx_meta(self, hash):
        self._get_json("tx", hash)

    def tx_id(self, hash):
        """Return transaction id."""
        return self.tx_field(hash, "id")

    def tx_owner(self, hash):
        """Return transaction owner."""
        return self.tx_field(hash, "owner")

    def tx_tags(self, hash):
        """Return transaction tags."""
        return self.tx_field(hash, "tags")

    def tx_target(self, hash):
        """Return transaction target."""
        return self.tx_field(hash, "target")

    # def tx_quantity(self, hash):
    #     """Return transaction quantity."""
    #     return self.tx_field(hash, "quantity")

    # def tx_data_root(self, hash):
    #     """Return transaction data root."""
    #     return self.tx_field(hash, "data_root")

    def tx_data_size(self, hash):
        """Return transaction data size."""
        return int(self.tx_field(hash, "data_size"))

    def tx_data(self, hash):
        """
        Return transaction data.

        The endpoint serves data regardless of how it was uploaded.
        """
        return self.tx_field(hash, "data")

    def tx_signature(self, hash):
        """Return transaction signature."""
        return self.tx_field(hash, "signature")

    # def tx_reward(self, hash):
    #     """Return transaction reward."""
    #     return self.tx_field(hash, "reward")

    # def height(self):
    #     """Return the current block hieght."""
    #     response = self._get("height")
    #     return int(response.text)

    def data(self, txid, ext="", range=None, timeout=60):
        """
        Get the decoded data from a transaction.

        This is roughly just an alias for tx_data_html.

        The transaction is pending: Pending
        The provided transaction ID is not valid or the field name is not valid: Invalid hash.
        A transaction with the given ID could not be found: Not Found.
        """
        if range is not None:
            headers = {"Range": f"bytes={range[0]}-{range[1]}"}
        else:
            headers = {}
        response = self._get(txid + ext, headers=headers, timeout=timeout)

        return response.content

    def graphql(self, query):
        response = self._post_json(
            {"operationName": None, "query": query, "variables": {}}, "graphql"
        )
        return response
