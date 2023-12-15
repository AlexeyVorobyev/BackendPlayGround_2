from pydantic import BaseModel


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


class PartialSectorEditDto(BaseModel):
    name: str | None
    description: str | None
