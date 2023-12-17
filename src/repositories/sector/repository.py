from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.sector.filter import SectorFilter
from src.models.sector.model import SectorModel
from src.utils.decorators.singleton import singleton


@singleton
class SectorRepository(SQLAlchemyRepository[SectorModel, SectorFilter]):
    _model = SectorModel
