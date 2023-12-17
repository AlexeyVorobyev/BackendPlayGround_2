from pydantic import BaseModel

from src.dtos.get_all.dto import GetAllDTO
from src.dtos.measure.dto import MeasureDTO
from src.utils.decorators.builder import builder


class ParameterDTO(BaseModel):
    id: str
    name: str
    measure: MeasureDTO


class ParameterAddDTO(BaseModel):
    name: str
    measure_id: str


class ParameterEditDTO(BaseModel):
    name: str
    measure_id: str


class ParameterPartialEditDTO(BaseModel):
    name: str | None
    measure_id: str | None


class ParameterGetAllDTO(GetAllDTO):
    data: list[ParameterDTO]


@builder
class ParameterGetAllDTOBuilder:
    _model = ParameterGetAllDTO
    _attr_total_pages: int
    _attr_total_elements: int
    _attr_current_page: int
    _attr_has_next_page: bool
    _attr_data: list[ParameterDTO]
