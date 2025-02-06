"""
Utility functions for the Irys integration.
"""

from irys_sdk.builder import Builder
from irys_sdk.client import Uploader
from irys_sdk.bundle.tags import Tags
import hashlib
import logging
from typing import Any, Dict


DEFAULT_BUNDLER_NODE = "https://uploader.irys.xyz"
DEFAULT_GATEWAY = "https://gateway.irys.xyz"
DEFAULT_TOKEN = "ethereum"


# max single tx size (TODO remove once chunking is implemented)
MAX_TX_BYTES = 50 * 1000 * 1000

log = logging.getLogger(__name__)


def get_tags_dict(tag_dicts: list[dict[str, str]]) -> dict[str, str]:
    """
    Helper function to merge a list of tag dicts into
    a single dictionary.

    Args:
        tag_dicts(list[dict[str, str]): a list of tag dicts with
        keys 'name' and 'value' corresponding to the name and
        value of the tag respectively.

    Returns:
        dict[str, str]: a key value dict mapping tag name to tag value
    """
    tags: dict[str, str] = {item["name"]: item["value"] for item in tag_dicts}
    return tags


def edge_unix_ts(edge: dict[str, Any]) -> float:
    """
    Helper function to extract the unix time stamp from an
    Irys transaction edge. See https://uploader.irys.xyz/graphql for the
    Irys graphql schema.

    Args:
        edge (dict[str, Any]): a transaction edge object

    Returns:
        float: unix timestamp in seconds
    """
    # sort matching manifests by time, get latest
    tag_dicts: list[dict[str, str]] = edge["node"]["tags"]
    return float(get_tags_dict(tag_dicts)["Unix-Time"])


def get_sha256_digest(file_path: str) -> str:
    """Helper function that computes the digest
    of a file in binary mode to handle potentially
    large files.

    Args:
        file_path (str): path to a file

    Returns:
        str: hex string representing the sha256
    """
    h = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


def from_tags_dict(tags: Dict[str, str]) -> Tags:
    return list(tags.items())


def init_irys(
    wallet: str, token: str = "ethereum", bundler_url: str = DEFAULT_BUNDLER_NODE
) -> Uploader:
    wallet2 = try_read_file(wallet)
    return Builder(token).wallet(wallet2).url(bundler_url).build()


def try_read_file(path_or_value: str) -> str:
    try:
        with open(path_or_value, 'r') as f:
            content = f.read()
            return content if content else path_or_value
    except:
        return path_or_value


def ensure_str(value: str | bytes) -> str:
    if isinstance(value, bytes):
        return value.decode('utf-8')
    return value
