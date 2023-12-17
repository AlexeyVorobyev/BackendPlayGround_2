from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.region.filter import RegionFilter
from src.models.region.model import RegionModel
from src.utils.decorators.singleton import singleton


@singleton
class RegionRepository(SQLAlchemyRepository[RegionModel, RegionFilter]):
    _model = RegionModel

