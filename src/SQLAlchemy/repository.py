from typing import Generic, TypeVar, Type

from sqlalchemy import select, insert, delete, update, func
from sqlalchemy.orm import Session
from src.SQLAlchemy.base import Base
from src.SQLAlchemy.connection import PostgreAlchemyConnection
from src.utils.classes.abstract_repository import AbstractRepository
from src.utils.classes.config import Config

Model = TypeVar('Model')


class SQLAlchemyRepository(Generic[Model], AbstractRepository[Model]):
    _model: Model = None
    _session_maker = PostgreAlchemyConnection(Config()).session_maker

    def total_elements(self):
        session: Session = self._session_maker()
        statement = select([func.count()]).select_from(self._model)
        query_result = session.execute(statement)
        result = query_result.scalar()
        return result

    def get_all(self, page: int = 0, per_page: int = 8):
        session: Session = self._session_maker()
        statement = select(self._model).offset(page * per_page).limit(per_page)
        query_result = session.execute(statement)
        result = [item[0] for item in query_result.all()]
        return result

    def get_by_id(self, id_arg: str):
        session: Session = self._session_maker()
        statement = select(self._model).where(self._model.id == id_arg)
        query_result = session.execute(statement)
        result = query_result.first()
        if result is None:
            return None
        else:
            return result[0]

    def create(self, data):
        session: Session = self._session_maker()
        statement = insert(self._model).values(**data).returning(self._model.id)
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result

    def update(self, id_arg, data):
        session: Session = self._session_maker()
        statement = (
            update(self._model)
            .where(self._model.id == id_arg)
            .values(**data)
            .returning(self._model.id)
        )
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result

    def delete_by_id(self, id_arg):
        session: Session = self._session_maker()
        statement = delete(self._model).where(self._model.id == id_arg).returning(self._model.id)
        query_result = session.execute(statement)
        session.commit()
        result = query_result.scalar_one()
        return result
