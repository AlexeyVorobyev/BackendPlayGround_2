from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.models.parameter.model import ParameterModel
from src.utils.decorators.singleton import singleton


@singleton
class ParameterRepository(SQLAlchemyRepository):
    _model = ParameterModel
