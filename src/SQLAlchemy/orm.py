from src.SQLAlchemy.base import Base
from src.SQLAlchemy.connection import PostgreAlchemyConnection
from src.utils.classes.config import Config
from src.utils.decorators.singleton import singleton


@singleton
class PostgreAlchemyORM:
    def __init__(self):
        self._session_maker = PostgreAlchemyConnection(Config()).session_maker
        self._engine = PostgreAlchemyConnection(Config()).engine

    def create_database(self):
        from src.models.region.model import RegionModel
        from src.models.sector.model import SectorModel
        from src.models.measure.model import MeasureModel
        from src.models.parameter.model import ParameterModel
        from src.models.record.model import RecordModel
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)

