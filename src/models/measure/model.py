from typing import List

from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.SQLAlchemy.base import Base
from src.models.parameter.model import ParameterModel


class MeasureModel(Base):
    __tablename__ = 'measure'

    id: Mapped[str] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    children: Mapped[List[ParameterModel]] = relationship()
