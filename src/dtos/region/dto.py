from pydantic import BaseModel

from src.dtos.get_all.dto import GetAllDTO


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
    name: str | None
    description: str | None


class RegionGetAllDTO(GetAllDTO):
    data: list[RegionDTO]
