from typing import TypedDict, NotRequired

from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.region.model import RegionModel


class SimpleFilterConfigTyped(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]
    name: NotRequired[list[str]]


class RegionFilter(SQLAlchemyFilter[RegionModel]):
    _model = RegionModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = config_arg
