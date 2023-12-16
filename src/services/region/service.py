import math
from uuid import UUID

from src.dtos.pagination.dto import PaginationDTO
from src.models.region.model import RegionModel
from src.repositories.region.repository import RegionRepository
from src.utils.decorators.singleton import singleton
from src.dtos.region.dto import RegionDTO, RegionAddDTO, RegionEditDTO, RegionPartialEditDTO, RegionGetAllDTO
from src.utils.functions.clear_dict_from_none import clear_dict_from_none


@singleton
class RegionService:
    _repository = RegionRepository()

    def get_regions(self, page, per_page) -> RegionGetAllDTO:
        pagination = PaginationDTO(**clear_dict_from_none(dict(page=page, per_page=per_page)))
        region_instances = self._repository.get_all(
            page=pagination.page,
            per_page=pagination.per_page
        )

        total_elements = self._repository.total_elements()

        return RegionGetAllDTO(
            total_pages=math.ceil(total_elements / pagination.per_page),
            total_elements=total_elements,
            data=[
                dict(RegionDTO(
                    id=str(instance.id),
                    name=instance.name,
                    description=instance.description
                )) for instance in region_instances
            ]
        )

    def create_region(self, region: RegionAddDTO) -> str:
        return self._repository.create(dict(region))

    def get_region(self, id_arg: str | None | UUID) -> RegionDTO:
        region_instance: RegionModel = self._repository.get_by_id(id_arg)

        if region_instance == None:
            raise Exception('No entities with specified id')

        return RegionDTO(
            id=str(region_instance.id),
            name=region_instance.name,
            description=region_instance.description
        )

    def delete_region(self, id_arg: str | None) -> str:
        return self._repository.delete_by_id(id_arg)

    def update_region(self, id_arg: str | None, region: RegionEditDTO | RegionPartialEditDTO) -> str:
        return self._repository.update(id_arg=id_arg, data=dict(region))
