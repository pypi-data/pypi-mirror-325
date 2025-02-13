from typing import Any, Literal

from pydantic import BaseModel


class ModificationSignature(BaseModel):
    residue_name: str
    residue_index: int
    modification_type: Literal["mask", "replace"]
    extra_information: dict[str, Any] = {}
