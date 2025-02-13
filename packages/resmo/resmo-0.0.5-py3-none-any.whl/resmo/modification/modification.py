from collections.abc import Generator

from pydantic import BaseModel

from ..protein_model import ProteinModel
from ..util import TemporaryFilePath
from .signature import ModificationSignature


class ModifiedProteinData(BaseModel):
    protein_data: str
    modification_signature: ModificationSignature

    def make_data_temp_file(self, ext: str):
        return TemporaryFilePath(ext, self.protein_data)


class ModificationType:
    def apply_all(
        self, protein_model: type[ProteinModel]
    ) -> Generator[ModifiedProteinData, None, None]:
        raise NotImplementedError
