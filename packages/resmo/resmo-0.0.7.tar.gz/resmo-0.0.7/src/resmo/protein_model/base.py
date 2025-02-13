from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel


class Residue(BaseModel):
    name: str
    id: int


class ProteinModel(ABC):
    """
    An abstract base class for interfacing with raw string data
    in file formats for protein structures.
    """

    @abstractmethod
    def __str__(self) -> str:
        """
        Return the string representation of the protein model.

        Returns:
            str: The string representation of the protein model.
        """
        ...

    @classmethod
    @abstractmethod
    def from_file(cls, file_path: str | Path) -> "ProteinModel":
        """
        Read the contents of a protein file and return the protein model.

        Args:
            file_path (str | Path): The path to the file to read.

        Returns:
            ProteinStringModel: The protein model.
        """
        ...

    @property
    def source_file(self) -> str | None:
        """
        Return the path to the source file if there is one.

        Returns:
            str | None: The optional path to the source file.
        """
        return None

    @abstractmethod
    def remove_residue(
        self,
        id_: int,
        relabel_atoms: bool = True,
        relabel_substructures: bool = True,
        relabel_bonds: bool = True,
    ) -> "ProteinModel":
        """
        Return new valid file contents with the residue removed.

        Args:
            protein_string (str): The unmodified protein file content.
            id_ (int): The id of the residue to be removed.

        Returns:
            ProteinStringModel: The modified protein file content.
        """
        ...

    @abstractmethod
    def get_residues(
        self,
    ) -> list[Residue]:
        """
        Return a list of Residue objects for given protein file content.

        Returns:
            list[Residue]: The list of Residue objects.
        """
        ...
