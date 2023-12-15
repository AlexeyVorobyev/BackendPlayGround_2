from pydantic import BaseModel


class MeasureDTO(BaseModel):
    id: str
    name: str


class MeasureAddDTO(BaseModel):
    name: str


class MeasureEditDTO(BaseModel):
    name: str


class PartialMeasureEditDto(BaseModel):
    name: str | None
