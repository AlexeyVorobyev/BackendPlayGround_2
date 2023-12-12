from typing import Optional, List
from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.SQLAlchemy.base import Base
from src.models.record.model import RecordModel


class SectorModel(Base):
    __tablename__ = 'sector'

    id: Mapped[str] = mapped_column(UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    children: Mapped[List[RecordModel]] = relationship()
