from typing import TypedDict, NotRequired
from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.measure.model import MeasureModel


class SimpleFilterConfigTyped(TypedDict):
    name: NotRequired[str]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]
    name: NotRequired[list[str]]


class MeasureFilter(SQLAlchemyFilter[MeasureModel]):
    _model = MeasureModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = config_arg
