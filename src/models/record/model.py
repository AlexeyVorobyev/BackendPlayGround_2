import datetime
from typing import Optional

from sqlalchemy import String, UUID, ForeignKey, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from src.SQLAlchemy.base import Base
from src.utils.decorators.add_repr import add_repr


@add_repr
class RecordModel(Base):
    __tablename__ = 'record'

    id: Mapped[Optional[str]] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))
    value: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=text("TIMEZONE('utc', now())"))
    parameter_id: Mapped[str] = mapped_column(ForeignKey('parameter.id'))
    region_id: Mapped[str] = mapped_column(ForeignKey('region.id'))
    sector_id: Mapped[str] = mapped_column(ForeignKey('sector.id'))


