from fastapi import APIRouter

from src.dtos.parameter.dto import ParameterGetAllDTO, ParameterAddDTO, ParameterDTO, ParameterEditDTO, \
    ParameterPartialEditDTO
from src.services.parameter.service import ParameterService

router = APIRouter(
    prefix="/parameter",
    tags=["parameter"],
)


class ParameterController:
    @staticmethod
    @router.get("")
    def get_parameters(
            page: int | None = None,
            per_page: int | None = None,
            simple_filter: str | None = None
    ) -> ParameterGetAllDTO:
        return ParameterService().get_parameters(page, per_page, simple_filter)

    @staticmethod
    @router.post("")
    def add_parameter(parameter: ParameterAddDTO):
        return ParameterService().create_parameter(parameter)

    @staticmethod
    @router.delete("/{id_arg}")
    def delete_parameter(id_arg: str):
        return ParameterService().delete_parameter(id_arg)

    @staticmethod
    @router.get("/{id_arg}")
    def get_region(id_arg: str) -> ParameterDTO:
        return ParameterService().get_parameter(id_arg)

    @staticmethod
    @router.put("/{id_arg}")
    def replace_region(id_arg: str, parameter: ParameterEditDTO):
        return ParameterService().update_parameter(id_arg=id_arg, parameter=parameter)

    @staticmethod
    @router.patch("/{id_arg}")
    def replace_region(id_arg: str, parameter: ParameterPartialEditDTO):
        return ParameterService().update_parameter(id_arg=id_arg, parameter=parameter)
