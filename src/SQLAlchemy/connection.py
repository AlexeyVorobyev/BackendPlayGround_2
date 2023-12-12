from abc import ABC, abstractmethod
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from src.SQLAlchemy.base import Base
from src.utils.config import config


class AlchemyConnection(ABC):
    @abstractmethod
    def create_database(self):
        pass


class PostgreAlchemyConnection(AlchemyConnection):
    def __init__(self, config_arg):
        self._url = f'postgresql://{config_arg.db_pg_user}:{config_arg.db_pg_password}@{config_arg.db_pg_host}:{config_arg.db_pg_port}/{config_arg.db_pg_name}'
        self._engine = sqlalchemy.create_engine(
            url=self._url,
            echo=True
        )
        self._session_factory = sessionmaker(self._engine)

    def create_database(self):
        from src.models.measure.model import MeasureModel
        from src.models.parameter.model import ParameterModel
        from src.models.region.model import RegionModel
        from src.models.sector.model import SectorModel
        from src.models.record.model import RecordModel
        session = self._session_factory()
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)


postgre_alchemy_connection = PostgreAlchemyConnection(config)
