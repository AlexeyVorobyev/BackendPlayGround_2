import math
from typing import Any

from src.dtos.measure.dto import (
    MeasureGetAllDTO,
    MeasureGetAllDTOBuilder,
    MeasureAddDTO,
    MeasureDTO,
    MeasureEditDTO,
    MeasurePartialEditDTO)
from src.dtos.pagination.dto import PaginationDTO
from src.filters.measure.filter import MeasureFilter
from src.repositories.measure.repository import MeasureRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none, clear_nested_dict_from_none


@singleton
class MeasureService:
    _repository = MeasureRepository()

    def get_measures(self, page, per_page, simple_filter) -> MeasureGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        measure_filter_instance = MeasureFilter(clear_nested_dict_from_none({
            'simple_filter': {
                'name': simple_filter,
            }
        }))

        measure_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=measure_filter_instance
        )

        measure_get_all_builder: Any = MeasureGetAllDTOBuilder()

        return (
            measure_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=measure_filter_instance))
            .total_pages(math.ceil(measure_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(MeasureDTO(
                    id=str(instance.id),
                    name=instance.name,
                )) for instance in measure_instances
            ])
            .has_next_page(pagination.page + 1 < measure_get_all_builder.attr_total_pages())
            .build()
        )

    def create_measure(self, region: MeasureAddDTO) -> str:
        return self._repository.create(dict(region))

    def get_measure(self, id_arg: str) -> MeasureDTO:
        measure_instance = self._repository.get_by_id(id_arg)

        if measure_instance is None:
            raise Exception('No entities with provided id')

        return MeasureDTO(
            id=str(measure_instance.id),
            name=measure_instance.name,
            description=measure_instance.description
        )

    def delete_measure(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_measure(self, id_arg: str | None, measure: MeasureEditDTO | MeasurePartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(measure))
