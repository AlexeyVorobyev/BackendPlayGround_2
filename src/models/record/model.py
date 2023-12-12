import datetime

from sqlalchemy import String, UUID, ForeignKey, DateTime, func, text, Table
from sqlalchemy.orm import Mapped, mapped_column
from src.SQLAlchemy.base import Base


class RecordModel(Base):
    __tablename__ = 'record'

    id: Mapped[str] = mapped_column(UUID, primary_key=True)
    value: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"))
    parameter_id: Mapped[str] = mapped_column(ForeignKey('parameter.id'))
    region_id: Mapped[str] = mapped_column(ForeignKey('region.id'))
    sector_id: Mapped[str] = mapped_column(ForeignKey('sector.id'))

