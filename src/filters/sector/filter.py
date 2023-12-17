from typing import TypedDict, NotRequired

from src.SQLAlchemy.filter import SQLAlchemyFilter
from src.models.sector.model import SectorModel


class SimpleFilterConfigTyped(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]


class ConfigTyped(TypedDict):
    simple_filter: NotRequired[SimpleFilterConfigTyped]
    id: NotRequired[list[str]]
    name: NotRequired[list[str]]


class SectorFilter(SQLAlchemyFilter[SectorModel]):
    _model = SectorModel

    def __init__(self, config_arg: ConfigTyped):
        self._config = config_arg
