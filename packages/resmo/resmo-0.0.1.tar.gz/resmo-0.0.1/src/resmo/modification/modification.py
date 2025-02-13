from collections.abc import Generator

from pydantic import BaseModel

from ..protein_model import ProteinModel
from .signature import ModificationSignature


class ModifiedProteinData(BaseModel):
    protein_data: str
    modification_signature: ModificationSignature


class ModificationType:
    def apply_all(
        self, protein_model: type[ProteinModel]
    ) -> Generator[ModifiedProteinData, None, None]:
        raise NotImplementedError
