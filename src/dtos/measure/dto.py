from pydantic import BaseModel


class RegionDTO(BaseModel):
    id: str
    name: str


class RegionAddDTO(BaseModel):
    name: str


class RegionEditDTO(BaseModel):
    name: str


class PartialRegionEditDto(BaseModel):
    name: str | None
