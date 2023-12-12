from typing import List

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.SQLAlchemy.base import Base
from src.models.record.model import RecordModel


class ParameterModel(Base):
    __tablename__ = 'parameter'

    id: Mapped[str] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    measure_id: Mapped[str] = mapped_column(ForeignKey('measure.id'))
    children: Mapped[List[RecordModel]] = relationship()
