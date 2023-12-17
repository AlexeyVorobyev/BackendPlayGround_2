from src.SQLAlchemy.repository import SQLAlchemyRepository
from src.filters.parameter.filter import ParameterFilter
from src.models.parameter.model import ParameterModel
from src.utils.decorators.singleton import singleton


@singleton
class ParameterRepository(SQLAlchemyRepository[ParameterModel, ParameterFilter]):
    _model = ParameterModel
