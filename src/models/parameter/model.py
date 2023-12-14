from typing import List, Optional

from sqlalchemy import String, UUID, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.SQLAlchemy.base import Base
from src.models.record.model import RecordModel
from src.utils.decorators.add_repr import add_repr


@add_repr
class ParameterModel(Base):
    __tablename__ = 'parameter'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    measure_id: Mapped[str] = mapped_column(ForeignKey('measure.id'))
    children: Mapped[List[RecordModel]] = relationship()

n = ParameterModel()