from collections.abc import Generator, Iterable
from pathlib import Path

from resmo.modification import ModificationType
from resmo.modification.modification import ModifiedProteinData
from resmo.protein_model import ProteinModel


# script main method
def generate_modified_data(
    protein_file_paths: Iterable[str | Path],
    protein_model_cls: type[ProteinModel],
    modification: ModificationType,
) -> Generator[ModifiedProteinData, None, None]:
    """
    Generate and yield modified protein file contents on the fly.

    Args:
        protein_file_paths (Iterable[str  |  Path]): Paths to files that describe the unmodified proteins.
        protein_model (type[ProteinStringModel]): The protein file format model to expect.
        modification_type (type[ModificationType]): The type of modification to apply.

    Yields:
        ModifiedProteinData: The modified protein file contents and the modification signature wrapped in a ModifiedProteinData object.
    """
    for protein_fp in protein_file_paths:
        protein_model = protein_model_cls.from_file(protein_fp)
        yield from modification.apply_all(protein_model)


if __name__ == "__main__":
    from resmo.modification.mask_residue import MaskResidue
    from resmo.protein_model import Mol2ProteinModel

    for file_content in generate_modified_data(
        protein_file_paths=["tests/data/5371_pocket.mol2"],
        protein_model_cls=Mol2ProteinModel,
        modification=MaskResidue(),
    ):
        print(file_content.protein_data)
        print(file_content.modification_signature)
        break
