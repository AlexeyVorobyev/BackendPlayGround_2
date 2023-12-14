from typing import List, Optional

from sqlalchemy import String, UUID, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.SQLAlchemy.base import Base
from src.models.parameter.model import ParameterModel
from src.utils.decorators.add_repr import add_repr


@add_repr
class MeasureModel(Base):
    __tablename__ = 'measure'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    children: Mapped[List[ParameterModel]] = relationship()
