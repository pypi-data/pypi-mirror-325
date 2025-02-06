from __future__ import annotations

from typing import Dict, NewType

from pydantic import BaseModel

IrysAddress = NewType(
    "IrysAddress",
    str,
)
"""Type alias for Irys addresses, represented as strings."""

IrysTransactionId = NewType("IrysTransactionId", str)
"""Type alias for Irys transaction IDs, represented as strings."""

Tags = Dict[str, str]
"""Type alias for a dictionary of tags, where both keys and values are strings."""


class IrysRepoId(BaseModel):
    """
    A class representing a repository identifier on Irys.

    Attributes:
        owner (IrysAddress): The owner of the repository.
        name (str): The name of the repository.
    """

    owner: IrysAddress
    name: str

    @classmethod
    def from_str(cls, _id: str) -> IrysRepoId:
        """
        Create a IrysRepoId instance from a string.

        Args:
            _id (str): A string in the format 'owner/name'.

        Returns:
            IrysRepoId: An instance of IrysRepoId with the owner and name extracted from the
            input string.
        """
        owner, name = _id.split("/")
        return cls(owner=IrysAddress(owner), name=name)


class LargeFileManifest(BaseModel):
    """
    A class to represent a manifest file for a large file uploaded in sections.

    Attributes:
        files (Dict[str, str]): A dictionary of file names and their transaction IDs.
        size (int): The total size of the file.
    """

    size: int
    files: Dict[str, str]
