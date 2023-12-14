from typing import Optional, List
from sqlalchemy import String, UUID, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.SQLAlchemy.base import Base
from src.models.record.model import RecordModel
from src.utils.decorators.add_repr import add_repr


@add_repr
class SectorModel(Base):
    __tablename__ = 'sector'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    children: Mapped[List[RecordModel]] = relationship()
