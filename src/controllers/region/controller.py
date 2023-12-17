from fastapi import APIRouter
from src.services.region.service import RegionService
from src.dtos.region.dto import RegionAddDTO, RegionEditDTO, RegionPartialEditDTO, RegionDTO, RegionGetAllDTO

router = APIRouter(
    prefix="/region",
    tags=["region"],
)


class RegionController:
    @staticmethod
    @router.get("")
    def get_regions(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> RegionGetAllDTO:
        return RegionService().get_regions(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_region(region: RegionAddDTO):
        return RegionService().create_region(region)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_region(id_arg: str):
        return RegionService().delete_region(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_region(id_arg: str) -> RegionDTO:
        return RegionService().get_region(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_region(id_arg: str, region: RegionEditDTO):
        return RegionService().update_region(id_arg=id_arg, region=region)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_region(id_arg: str, region: RegionPartialEditDTO):
        return RegionService().update_region(id_arg=id_arg, region=region)
