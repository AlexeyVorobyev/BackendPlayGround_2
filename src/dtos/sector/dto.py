from typing import Optional
from pydantic import BaseModel
from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class SectorDTO(BaseModel):
    id: str
    name: str
    description: str


class SectorAddDTO(BaseModel):
    name: str
    description: str


class SectorEditDTO(BaseModel):
    name: str
    description: str


class SectorPartialEditDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]


class SectorGetAllDTO(GetAllDTO):
    data: list[SectorDTO]


@builder
class SectorGetAllDTOBuilder:
    _model = SectorGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[SectorDTO]
