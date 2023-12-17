from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.measure.filter import MeasureFilter
from src.models.measure.model import MeasureModel
from src.utils.decorators.singleton import singleton


@singleton
class MeasureRepository(SQLAlchemyRepository[MeasureModel, MeasureFilter]):
    _model = MeasureModel
