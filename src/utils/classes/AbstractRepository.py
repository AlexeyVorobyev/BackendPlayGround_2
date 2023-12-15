from abc import ABC, abstractmethod
from typing import TypeVar

modelInstance = TypeVar('modelInstance')


class AbstractRepository(ABC):
    _model: modelInstance
    _collection: list[modelInstance]
    _collection_length: int

    @property
    @abstractmethod
    def collection_length(self) -> int:
        pass

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
    def create(self, data: dict) -> modelInstance:
        pass

    @abstractmethod
    def update(self, id_arg: str, data: dict):
        pass

    @abstractmethod
    def delete_by_id(self, id_arg: str):
        pass
