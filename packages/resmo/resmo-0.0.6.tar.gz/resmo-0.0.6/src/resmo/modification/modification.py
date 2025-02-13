from collections.abc import Generator
import tempfile

from pydantic import BaseModel

from ..protein_model import ProteinModel
from .signature import ModificationSignature


class ModifiedProteinData(BaseModel):
    protein_data: str
    modification_signature: ModificationSignature

    def temp_file_with_protein_data(self, ext: str):
        return tempfile.TemporaryFile(mode="wt", suffix=ext)


class ModificationType:
    def apply_all(
        self, protein_model: type[ProteinModel]
    ) -> Generator[ModifiedProteinData, None, None]:
        raise NotImplementedError
