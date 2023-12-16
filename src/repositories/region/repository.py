from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.models.region.model import RegionModel
from src.utils.decorators.singleton import singleton


@singleton
class RegionRepository(SQLAlchemyRepository[RegionModel]):
    _model = RegionModel


some = RegionRepository().get_all()
