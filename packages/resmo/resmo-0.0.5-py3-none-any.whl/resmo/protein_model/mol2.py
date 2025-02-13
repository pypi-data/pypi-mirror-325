import copy
import re
from enum import Enum
from itertools import chain, tee
from pathlib import Path
from typing import Optional

# from .base import ProteinStringModel
from pydantic import BaseModel, Field

from resmo.protein_model.base import ProteinModel, Residue

_TRIPOS_SECTION_HEADER_PATTERN = re.compile(r"@\<TRIPOS\>(?P<section_name>\w+)\s*")


def _remove_empty_lines(strobj: str) -> str:
    return "\n".join([line for line in strobj.split("\n") if line.strip()])


def _remove_comments(strobj: str, comment_char: str = "#") -> str:
    return "\n".join(
        [
            line
            for line in strobj.split("\n")
            if not line.lstrip().startswith(comment_char)
        ]
    )


class Mol2Atom(BaseModel):
    atom_id: int = Field(..., description="Unique atom ID")
    atom_name: str = Field(..., description="Atom name")
    x: float = Field(..., description="X coordinate")
    y: float = Field(..., description="Y coordinate")
    z: float = Field(..., description="Z coordinate")
    atom_type: str = Field(..., description="Tripos atom type")
    subst_id: Optional[int] = Field(None, description="Substructure ID")
    subst_name: Optional[str] = Field(None, description="Substructure name")
    charge: Optional[float] = Field(None, description="Partial charge")


class Mol2Bond(BaseModel):
    bond_id: int = Field(..., description="Unique bond ID")
    origin_atom_id: int = Field(..., description="First atom ID")
    target_atom_id: int = Field(..., description="Second atom ID")
    bond_type: str = Field(..., description="Bond type")


class Mol2Substructure(BaseModel):
    subst_id: int = Field(..., description="Substructure ID")
    subst_name: str = Field(..., description="Substructure name")
    root_atom_id: int = Field(..., description="Root atom ID")
    subst_type: Optional[str] = Field(None, description="Substructure type")
    dictionary: Optional[int] = Field(None, description="Dictionary entry")
    chain: Optional[str] = Field(None, description="Protein chain identifier")
    subst_type: Optional[str] = Field(None, description="Substructure subtype")
    inter_bonds: Optional[int] = Field(None, description="Inter-substructure bonds")
    status: Optional[str] = Field(None, description="Status indicators")


class Mol2Molecule(BaseModel):
    name: str = Field(..., description="Molecule name")
    num_atoms: int = Field(..., description="Number of atoms")
    num_bonds: int = Field(..., description="Number of bonds")
    num_subst: int = Field(..., description="Number of substructures")
    num_feat: int = Field(..., description="Number of features")
    num_sets: int = Field(..., description="Number of sets")
    mol_type: str = Field(..., description="Molecule type")
    charge_type: str = Field(..., description="Charge type")
    status_bits: Optional[str] = Field(None, description="Status bits")
    atoms: list[Mol2Atom] = Field(..., description="List of atoms")
    bonds: list[Mol2Bond] = Field(..., description="List of bonds")
    substructures: Optional[list[Mol2Substructure]] = Field(
        None, description="List of substructures"
    )


class Mol2Fields(Enum):
    ATOM_ID = "atom_id"
    ATOM_NAME = "atom_name"
    ATOM_TYPE = "atom_type"
    BOND_ID = "bond_id"
    BOND_TYPE = "bond_type"
    CHAIN = "chain"
    CHARGE = "charge"
    DICTIONARY = "dictionary"
    IGNORE = "IGNORE"
    INTER_BONDS = "inter_bonds"
    ORIGIN_ATOM_ID = "origin_atom_id"
    ROOT_ATOM_ID = "root_atom_id"
    STATUS = "status"
    SUBST_ID = "subst_id"
    SUBST_NAME = "subst_name"
    SUBST_TYPE = "subst_type"
    TARGET_ATOM_ID = "target_atom_id"
    X = "x"
    Y = "y"
    Z = "z"


KLIFS_MOL2_ATOM_SCHEMA = [
    Mol2Fields.ATOM_ID,
    Mol2Fields.ATOM_NAME,
    Mol2Fields.X,
    Mol2Fields.Y,
    Mol2Fields.Z,
    Mol2Fields.ATOM_TYPE,
    Mol2Fields.SUBST_ID,
    Mol2Fields.SUBST_NAME,
    Mol2Fields.CHARGE,
    Mol2Fields.IGNORE,
]

KLIFS_MOL2_BOND_SCHEMA = [
    Mol2Fields.BOND_ID,
    Mol2Fields.ORIGIN_ATOM_ID,
    Mol2Fields.TARGET_ATOM_ID,
    Mol2Fields.BOND_TYPE,
    Mol2Fields.IGNORE,
]

KLIFS_MOL2_SUBST_SCHEMA = [
    Mol2Fields.SUBST_ID,
    Mol2Fields.SUBST_NAME,
    Mol2Fields.ROOT_ATOM_ID,
    Mol2Fields.SUBST_TYPE,
    Mol2Fields.DICTIONARY,
    Mol2Fields.CHAIN,
    Mol2Fields.SUBST_TYPE,
    Mol2Fields.INTER_BONDS,
    Mol2Fields.IGNORE,
]

KLIFS_MOL2_MOLECULE_SCHMEA = [
    "name",
    ("num_atoms", "num_bonds", "num_subst", "num_feat", "num_sets"),
    "mol_type",
    "charge_type",
]


def _parse_line_objs(
    lines: str, line_schema: list[Mol2Fields], model_cls: type[BaseModel]
):
    objs = []
    for line in lines:
        atom = {}
        for field, value in zip(line_schema, line.strip().split()):
            if field == Mol2Fields.IGNORE:
                continue
            atom[field.value] = value
        atom = model_cls(**atom)
        objs.append(atom)
    return objs


def _parse_molecule_lines(lines: list[str]):
    mol_dict = {}
    for line, key in zip(lines, KLIFS_MOL2_MOLECULE_SCHMEA):
        if isinstance(key, tuple):
            values = line.strip().split()
            mol_dict.update(dict(zip(key, values)))
            continue
        value = line.strip()
        mol_dict[key] = value
    return mol_dict


def parse_mol2_file(
    mol2_object: str | Path,
    atom_line_schema: list[Mol2Fields] | None = None,
    bond_line_schema: list[Mol2Fields] | None = None,
    subst_line_schema: list[Mol2Fields] | None = None,
) -> Mol2Molecule:
    if isinstance(mol2_object, Path):
        mol2_object = mol2_object.read_text()
    if atom_line_schema is None:
        atom_line_schema = KLIFS_MOL2_ATOM_SCHEMA
    if bond_line_schema is None:
        bond_line_schema = KLIFS_MOL2_BOND_SCHEMA
    if subst_line_schema is None:
        subst_line_schema = KLIFS_MOL2_SUBST_SCHEMA

    mol2_object = _remove_empty_lines(mol2_object)
    mol2_object = _remove_comments(mol2_object)
    matches, next_matches = tee(_TRIPOS_SECTION_HEADER_PATTERN.finditer(mol2_object), 2)
    next(next_matches)
    mol_attrs = {}
    for match, next_match in zip(matches, chain(next_matches, [None])):
        j_start = match.end()
        j_end = next_match.start() if next_match else len(mol2_object)
        section_lines = mol2_object[j_start:j_end].strip().split("\n")
        section_type = match.group("section_name")
        if section_type == "MOLECULE":
            mol_attrs.update(_parse_molecule_lines(section_lines))
        elif section_type == "ATOM":
            mol_attrs["atoms"] = _parse_line_objs(
                section_lines, atom_line_schema, Mol2Atom
            )
        elif section_type == "BOND":
            mol_attrs["bonds"] = _parse_line_objs(
                section_lines, bond_line_schema, Mol2Bond
            )
        elif section_type == "SUBSTRUCTURE":
            mol_attrs["substructures"] = _parse_line_objs(
                section_lines, subst_line_schema, Mol2Substructure
            )
    return Mol2Molecule(**mol_attrs)


def write_mol2_lines(
    molecule: Mol2Molecule,
) -> list[str]:
    lines = [
        "@<TRIPOS>MOLECULE",
        f"{molecule.name}",
        f"{molecule.num_atoms} {molecule.num_bonds} {molecule.num_subst} {molecule.num_feat} {molecule.num_sets}",
        f"{molecule.mol_type}",
        f"{molecule.charge_type}",
    ]

    lines.append("@<TRIPOS>ATOM")
    lines.extend(
        [
            f"{atom.atom_id} {atom.atom_name} {atom.x} {atom.y} {atom.z} {atom.atom_type} {atom.subst_id} {atom.subst_name} {atom.charge}"
            for atom in molecule.atoms
        ]
    )

    lines.append("@<TRIPOS>BOND")
    lines.extend(
        [
            f"{bond.bond_id} {bond.origin_atom_id} {bond.target_atom_id} {bond.bond_type}"
            for bond in molecule.bonds
        ]
    )

    lines.append("@<TRIPOS>SUBSTRUCTURE")
    lines.extend(
        [
            f"{subst.subst_id} {subst.subst_name} {subst.root_atom_id} {subst.subst_type} {subst.dictionary} {subst.chain} {subst.subst_type} {subst.inter_bonds}"
            for subst in molecule.substructures
        ]
    )
    return lines


def write_mol2_file(
    molecule: Mol2Molecule,
    fp: str | Path,
):
    mol2_lines = write_mol2_lines(molecule)
    with open(fp, "w") as f:
        f.write("\n".join(mol2_lines))


def relabel(objs: list[object], label_attr: str, zero: int = 1) -> dict[int, int]:
    def _relabel_one(obj, i):
        orig_id = getattr(obj, label_attr)
        setattr(obj, label_attr, i)
        return orig_id

    return {_relabel_one(obj, i): i for i, obj in enumerate(objs, start=zero)}


class Mol2ProteinModel(ProteinModel):
    mol2_file: Path
    molecule: Mol2Molecule

    @classmethod
    def from_file(cls, mol2_file: str | Path):
        mol2_file = Path(mol2_file)
        molecule = parse_mol2_file(mol2_file)
        return cls(mol2_file=mol2_file, molecule=molecule)

    def __init__(self, mol2_file: Path, molecule: Mol2Molecule):
        self.mol2_file = mol2_file
        self.molecule = molecule

    @property
    def source_file(self) -> str | None:
        return self.mol2_file.as_posix()

    def write(self, fp: str | Path):
        write_mol2_file(self.molecule, fp)

    def __str__(self):
        return "\n".join(write_mol2_lines(self.molecule))

    def remove_residue(
        self,
        id_: int,
        relabel_atoms: bool = True,
        relabel_substructures: bool = True,
        relabel_bonds: bool = True,
    ):
        modified_molecule = self.molecule.model_copy()

        subst_atom_ids = set()

        def _register(atom):
            is_subst_atom = atom.subst_id == id_
            if is_subst_atom:
                subst_atom_ids.add(atom.atom_id)
            return is_subst_atom

        modified_molecule.atoms = [
            atom for atom in modified_molecule.atoms if not _register(atom)
        ]
        modified_molecule.bonds = [
            bond
            for bond in modified_molecule.bonds
            if bond.origin_atom_id not in subst_atom_ids
            and bond.target_atom_id not in subst_atom_ids
        ]
        modified_molecule.substructures = [
            subst for subst in modified_molecule.substructures if subst.subst_id != id_
        ]
        if relabel_substructures:
            modified_molecule.substructures = copy.deepcopy(
                modified_molecule.substructures
            )
            subst_label_map = relabel(modified_molecule.substructures, "subst_id")
            for atom in modified_molecule.atoms:
                atom.subst_id = subst_label_map[atom.subst_id]
        if relabel_bonds:
            modified_molecule.bonds = copy.deepcopy(modified_molecule.bonds)
            relabel(modified_molecule.bonds, "bond_id")
        if relabel_atoms:
            modified_molecule.atoms = copy.deepcopy(modified_molecule.atoms)
            atom_label_map = relabel(modified_molecule.atoms, "atom_id")
            for bond in modified_molecule.bonds:
                bond.origin_atom_id = atom_label_map[bond.origin_atom_id]
                bond.target_atom_id = atom_label_map[bond.target_atom_id]
        modified_molecule.num_atoms = len(modified_molecule.atoms)
        modified_molecule.num_bonds = len(modified_molecule.bonds)
        modified_molecule.num_subst = len(modified_molecule.substructures)
        return Mol2ProteinModel(self.mol2_file, modified_molecule)

    def get_residues(self) -> list[Residue]:
        return [
            Residue(id=subst.subst_id, name=subst.subst_name)
            for subst in self.molecule.substructures
        ]


if __name__ == "__main__":
    mol2_file = Path("tests/data/test.mol2")
    print(mol2_file.absolute())
    molecule = parse_mol2_file(mol2_file)
    write_mol2_file(molecule, "tests/data/test2.mol2")

    content1 = mol2_file.read_text()
    content2 = Path("tests/data/test2.mol2").read_text()
    if content1 != content2:
        raise ValueError(content1, content2)

    model = Mol2ProteinModel.from_file(mol2_file)
    model.remove_residue(1)
