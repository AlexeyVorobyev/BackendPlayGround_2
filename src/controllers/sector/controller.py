from fastapi import APIRouter
from src.dtos.sector.dto import SectorGetAllDTO, SectorAddDTO, SectorDTO, SectorEditDTO, SectorPartialEditDTO
from src.services.sector.service import SectorService

router = APIRouter(
    prefix="/sector",
    tags=["sector"],
)


class SectorController:
    @staticmethod
    @router.get("")
    def get_sectors(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> SectorGetAllDTO:
        return SectorService().get_sectors(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_sector(region: SectorAddDTO):
        return SectorService().create_sector(region)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_sector(id_arg: str):
        return SectorService().delete_sector(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_sector(id_arg: str) -> SectorDTO:
        return SectorService().get_sector(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_sector(id_arg: str, sector: SectorEditDTO):
        return SectorService().update_sector(id_arg=id_arg, sector=sector)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_sector(id_arg: str, sector: SectorPartialEditDTO):
        return SectorService().update_sector(id_arg=id_arg, sector=sector)
