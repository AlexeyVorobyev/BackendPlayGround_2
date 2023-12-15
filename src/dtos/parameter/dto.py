from pydantic import BaseModel


class ParameterDTO(BaseModel):
    id: str
    name: str
    measure_id: str


class ParameterAddDTO(BaseModel):
    name: str
    measure_id: str


class ParameterEditDTO(BaseModel):
    name: str
    measure_id: str


class PartialParameterEditDto(BaseModel):
    name: str | None
    measure_id: str | None
