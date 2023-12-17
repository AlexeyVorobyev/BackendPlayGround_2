import math
from typing import Any

from src.dtos.measure.dto import MeasureDTO
from src.dtos.pagination.dto import PaginationDTO
from src.dtos.parameter.dto import (
    ParameterGetAllDTO,
    ParameterGetAllDTOBuilder,
    ParameterDTO,
    ParameterAddDTO,
    ParameterEditDTO,
    ParameterPartialEditDTO)
from src.filters.parameter.filter import ParameterFilter
from src.repositories.parameter.repository import ParameterRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none, clear_nested_dict_from_none


@singleton
class ParameterService:
    _repository = ParameterRepository()

    def get_parameters(self, page, per_page, simple_filter) -> ParameterGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        parameter_filter_instance = ParameterFilter(clear_nested_dict_from_none({
            'simple_filter': {
                'name': simple_filter,
            }
        }))

        parameter_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=parameter_filter_instance
        )

        parameter_get_all_builder: Any = ParameterGetAllDTOBuilder()

        return (
            parameter_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=parameter_filter_instance))
            .total_pages(math.ceil(parameter_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(ParameterDTO(
                    id=str(instance.id),
                    name=instance.name,
                    measure=dict(MeasureDTO(
                        id=str(instance.parent.id),
                        name=instance.parent.name
                    ))
                )) for instance in parameter_instances
            ])
            .has_next_page(pagination.page + 1 < parameter_get_all_builder.attr_total_pages())
            .build()
        )

    def create_parameter(self, parameter: ParameterAddDTO) -> str:
        return self._repository.create(dict(parameter))

    def get_parameter(self, id_arg: str) -> ParameterDTO:
        parameter_instance = self._repository.get_by_id(id_arg)

        if parameter_instance is None:
            raise Exception('No entities with provided id')

        return ParameterDTO(
            id=str(parameter_instance.id),
            name=parameter_instance.name,
            measure=dict(MeasureDTO(
                id=str(parameter_instance.parent.id),
                name=parameter_instance.parent.name
            ))
        )

    def delete_parameter(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_parameter(self, id_arg: str | None, parameter: ParameterEditDTO | ParameterPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(parameter))
