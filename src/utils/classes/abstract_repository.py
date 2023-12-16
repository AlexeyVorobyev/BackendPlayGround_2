from abc import ABC, abstractmethod
from typing import TypeVar, Generic

Model = TypeVar('Model')


class AbstractRepository(Generic[Model], ABC):
    _model: Model

    @abstractmethod
    def total_elements(self) -> int:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int) -> list[Model]:
        pass

    @abstractmethod
    def get_by_id(self, id_arg: str) -> Model | None:
        pass

    @abstractmethod
    def create(self, data: dict) -> Model:
        pass

    @abstractmethod
    def update(self, id_arg: str, data: dict):
        pass

    @abstractmethod
    def delete_by_id(self, id_arg: str):
        pass
