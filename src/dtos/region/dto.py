from pydantic import BaseModel


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


class PartialRegionEditDto(BaseModel):
    name: str | None
    description: str | None
