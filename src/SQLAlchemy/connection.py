import sqlalchemy
from src.utils.config import config
from abc import ABC, abstractproperty, abstractmethod
from sqlalchemy import create_engine, Engine


class AlchemyConnection(ABC):
    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @url.setter
    @abstractmethod
    def url(self, value: str):
        return value

    @abstractmethod
    def create_engine(self) -> Engine:
        pass


class PostgreAlchemyConnection(AlchemyConnection):
    def __init__(self, config_arg):
        self._url = f'postgresql://{config_arg.db_pg_user}:{config_arg.db_pg_password}\
        @{config_arg.db_pg_host}:{config_arg.db_pg_port}/{config_arg.db_pg_name}'

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    def create_engine(self) -> Engine:
        return sqlalchemy.create_engine(self._url)


postgre_alchemy_connection = PostgreAlchemyConnection(config)
postgre_alchemy_engine = postgre_alchemy_connection.create_engine()
