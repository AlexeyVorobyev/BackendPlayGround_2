import math
from typing import Any

from src.dtos.pagination.dto import PaginationDTO
from src.dtos.region.dto import (
    RegionDTO,
    RegionAddDTO,
    RegionEditDTO,
    RegionPartialEditDTO,
    RegionGetAllDTO,
    RegionGetAllDTOBuilder)
from src.filters.region.filter import RegionFilter
from src.repositories.region.repository import RegionRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none, clear_nested_dict_from_none


@singleton
class RegionService:
    _repository = RegionRepository()

    def get_regions(self, page, per_page, simple_filter) -> RegionGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        region_filter_instance = RegionFilter(clear_nested_dict_from_none({
            'simple_filter': {
                'name': simple_filter,
                'description': simple_filter
            }
        }))

        region_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=region_filter_instance
        )

        region_get_all_builder: Any = RegionGetAllDTOBuilder()

        return (
            region_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=region_filter_instance))
            .total_pages(math.ceil(region_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(RegionDTO(
                    id=str(instance.id),
                    name=instance.name,
                    description=instance.description
                )) for instance in region_instances
            ])
            .has_next_page(pagination.page + 1 < region_get_all_builder.attr_total_pages())
            .build()
        )

    def create_region(self, region: RegionAddDTO) -> str:
        return self._repository.create(dict(region))

    def get_region(self, id_arg: str) -> RegionDTO:
        region_instance = self._repository.get_by_id(id_arg)

        if region_instance is None:
            raise Exception('No entities with provided id')

        return RegionDTO(
            id=str(region_instance.id),
            name=region_instance.name,
            description=region_instance.description
        )

    def delete_region(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_region(self, id_arg: str | None, region: RegionEditDTO | RegionPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(region))
