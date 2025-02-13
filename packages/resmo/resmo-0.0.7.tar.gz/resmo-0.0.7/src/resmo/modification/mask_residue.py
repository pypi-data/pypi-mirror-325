from collections.abc import Generator

from ..protein_model import ProteinModel
from .modification import ModificationSignature, ModificationType, ModifiedProteinData


class MaskResidue(ModificationType):

    def apply_all(
        self,
        protein_model: ProteinModel,
    ) -> Generator[ModifiedProteinData, None, None]:
        for residue in protein_model.get_residues():
            modified_string = str(protein_model.remove_residue(residue.id))
            yield ModifiedProteinData(
                protein_data=modified_string,
                modification_signature=ModificationSignature(
                    source_file=protein_model.source_file,
                    residue_name=residue.name,
                    residue_index=residue.id,
                    modification_type="mask",
                ),
            )
