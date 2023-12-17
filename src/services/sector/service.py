import math
from typing import Any
from src.dtos.pagination.dto import PaginationDTO
from src.dtos.sector.dto import (
    SectorGetAllDTO,
    SectorGetAllDTOBuilder,
    SectorAddDTO,
    SectorDTO,
    SectorEditDTO,
    SectorPartialEditDTO)
from src.filters.sector.filter import SectorFilter
from src.repositories.sector.repository import SectorRepository
from src.utils.decorators.singleton import singleton
from src.utils.functions.clear_dict_from_none import clear_dict_from_none, clear_nested_dict_from_none


@singleton
class SectorService:
    _repository = SectorRepository()

    def get_sectors(self, page, per_page, simple_filter) -> SectorGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        sector_filter_instance = SectorFilter(clear_nested_dict_from_none({
            'simple_filter': {
                'name': simple_filter,
                'description': simple_filter
            }
        }))

        sector_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page,
            filter_instance=sector_filter_instance
        )

        sector_get_all_builder: Any = SectorGetAllDTOBuilder()

        return (
            sector_get_all_builder
            .total_elements(self._repository.total_elements(filter_instance=sector_filter_instance))
            .total_pages(math.ceil(sector_get_all_builder.attr_total_elements() / pagination.per_page))
            .current_page(pagination.page)
            .data([
                dict(SectorDTO(
                    id=str(instance.id),
                    name=instance.name,
                    description=instance.description
                )) for instance in sector_instances
            ])
            .has_next_page(pagination.page + 1 < sector_get_all_builder.attr_total_pages())
            .build()
        )

    def create_sector(self, sector: SectorAddDTO) -> str:
        return self._repository.create(dict(sector))

    def get_sector(self, id_arg: str) -> SectorDTO:
        sector_instance = self._repository.get_by_id(id_arg)

        if sector_instance is None:
            raise Exception('No entities with provided id')

        return SectorDTO(
            id=str(sector_instance.id),
            name=sector_instance.name,
            description=sector_instance.description
        )

    def delete_sector(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_sector(self, id_arg: str | None, sector: SectorEditDTO | SectorPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(sector))
