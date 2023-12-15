from pydantic import BaseModel


class RegionDTO(BaseModel):
    id: str
    name: str
    measure_id: str


class RegionAddDTO(BaseModel):
    name: str
    measure_id: str


class RegionEditDTO(BaseModel):
    name: str
    measure_id: str


class PartialRegionEditDto(BaseModel):
    name: str | None
    measure_id: str | None