from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.models.record.model import RecordModel
from src.utils.decorators.singleton import singleton


@singleton
class RecordRepository(SQLAlchemyRepository):
    _model = RecordModel
