from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.models.measure.model import MeasureModel
from src.utils.decorators.singleton import singleton


@singleton
class MeasureRepository(SQLAlchemyRepository):
    _model = MeasureModel
