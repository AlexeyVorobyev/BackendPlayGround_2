from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from src.dtos.get_all.dto import GetAllDTO
from src.utils.decorators.builder import builder


class MeasureDTO(BaseModel):
    id: str
    name: str


class MeasureAddDTO(BaseModel):
    name: str


class MeasureEditDTO(BaseModel):
    name: str


class MeasurePartialEditDTO(BaseModel):
    name: Optional[str]


class MeasureGetAllDTO(GetAllDTO):
    data: list[MeasureDTO]


@builder
class MeasureGetAllDTOBuilder:
    _model = MeasureGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[MeasureDTO]
