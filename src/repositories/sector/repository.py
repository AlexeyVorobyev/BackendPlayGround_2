from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.models.sector.model import SectorModel
from src.utils.decorators.singleton import singleton


@singleton
class RegionRepository(SQLAlchemyRepository):
    _model = SectorModel
