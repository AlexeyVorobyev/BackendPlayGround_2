from typing import Optional

from pydantic import BaseModel
from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class RegionDTO(BaseModel):
    id: str
    name: str
    description: str


class RegionAddDTO(BaseModel):
    name: str
    description: str


class RegionEditDTO(BaseModel):
    name: str
    description: str


class RegionPartialEditDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]


class RegionGetAllDTO(GetAllDTO):
    data: list[RegionDTO]


@builder
class RegionGetAllDTOBuilder:
    _model = RegionGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[RegionDTO]
