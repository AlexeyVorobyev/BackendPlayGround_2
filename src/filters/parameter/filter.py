from typing import TypedDict, NotRequired

from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.parameter.model import ParameterModel


class SimpleFilterConfigTyped(TypedDict):
    name: NotRequired[str]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]
    name: NotRequired[list[str]]
    measure_id: NotRequired[list[str]]


class ParameterFilter(SQLAlchemyFilter[ParameterModel]):
    _model = ParameterModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = config_arg
