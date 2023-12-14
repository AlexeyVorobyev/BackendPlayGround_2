from abc import ABC, abstractmethod
from typing import TypeVar

modelInstance = TypeVar('modelInstance')


class BaseRepository(ABC):
    _collection: list[modelInstance]

    @abstractmethod
    def _update_repository(self):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int) -> list[modelInstance]:
        pass

    @abstractmethod
    def get_by_id(self, id_arg: str) -> modelInstance | None:
        pass

    @abstractmethod
    def create(self, model_instance: modelInstance) -> bool:
        pass

    @abstractmethod
    def replace(self, id_arg: str, model_instance: modelInstance) -> bool:
        pass

    @abstractmethod
    def update(self, id_arg: str, model_instance: modelInstance) -> bool:
        pass

    @abstractmethod
    def delete_by_id(self, id_arg: str) -> bool:
        pass
