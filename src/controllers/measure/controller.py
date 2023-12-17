from fastapi import APIRouter

from src.dtos.measure.dto import (
    MeasureGetAllDTO,
    MeasureAddDTO,
    MeasureDTO,
    MeasureEditDTO,
    MeasurePartialEditDTO)
from src.services.measure.service import MeasureService

router = APIRouter(
    prefix="/measure",
    tags=["measure"],
)


class MeasureController:
    @staticmethod
    @router.get("")
    def get_measures(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> MeasureGetAllDTO:
        return MeasureService().get_measures(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_measure(measure: MeasureAddDTO):
        return MeasureService().create_measure(measure)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_measure(id_arg: str):
        return MeasureService().delete_measure(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_measure(id_arg: str) -> MeasureDTO:
        return MeasureService().get_measure(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_measure(id_arg: str, measure: MeasureEditDTO):
        return MeasureService().update_measure(id_arg=id_arg, measure=measure)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_measure(id_arg: str, measure: MeasurePartialEditDTO):
        return MeasureService().update_measure(id_arg=id_arg, measure=measure)
