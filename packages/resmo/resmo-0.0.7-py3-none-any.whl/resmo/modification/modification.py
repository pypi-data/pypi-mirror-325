import tempfile
from collections.abc import Generator

from pydantic import BaseModel

from ..protein_model import ProteinModel
from .signature import ModificationSignature


class ModifiedProteinData(BaseModel):
    protein_data: str
    modification_signature: ModificationSignature

    def temp_file_with_protein_data(self, ext: str):
        tf = tempfile.NamedTemporaryFile(mode="wt", suffix=ext)  # noqa: SIM115
        tf.write(self.protein_data)
        return tf


class ModificationType:
    def apply_all(
        self, protein_model: type[ProteinModel]
    ) -> Generator[ModifiedProteinData, None, None]:
        raise NotImplementedError
