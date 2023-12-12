from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.SQLAlchemy.base import Base


class RegionModel(Base):
    __tablename__ = 'region'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(500))

