from sqlalchemy import select, insert, delete, update
from sqlalchemy.orm import Session
from src.SQLAlchemy.base import Base
from src.SQLAlchemy.connection import PostgreAlchemyConnection
from src.utils.classes.AbstractRepository import AbstractRepository
from src.utils.classes.config import Config


class SQLAlchemyRepository(AbstractRepository):
    _model: Base = None
    _session_maker = PostgreAlchemyConnection(Config()).session_maker
    _collection = []
    _collection_length = 0

    def __init__(self):
        self._update_repository()

    @property
    def collection_length(self):
        return self._collection_length

    def _update_repository(self):
        session: Session = self._session_maker()
        statement = select(self._model)
        result = session.execute(statement)
        self._collection = [item[0] for item in result.all()]
        self._collection_length = len(self._collection)

    def get_all(self, page: int = 0, per_page: int = 8):
        result = []
        calc_end = len(self._collection) if len(self._collection) < per_page * (page + 1) else per_page * (page + 1)
        for i in range(per_page * page, calc_end):
            result.append(self._collection[i])
        return result

    def get_by_id(self, id_arg: str):
        for instance in self._collection:
            if instance.id == id_arg:
                return instance
        return None

    def create(self, data):
        session: Session = self._session_maker()
        statement = insert(self._model).values(**data).returning(self._model.id)
        res = session.execute(statement)
        session.commit()
        self._update_repository()
        return res.scalar_one()

    def update(self, id_arg, data):
        session: Session = self._session_maker()
        statement = (
            update(self._model)
            .where(self._model.id == id_arg)
            .values(**data)
            .returning(self._model.id)
        )
        res = session.execute(statement)
        session.commit()
        self._update_repository()
        return res.scalar_one()

    def delete_by_id(self, id_arg):
        session: Session = self._session_maker()
        statement = delete(self._model).where(self._model.id == id_arg).returning(self._model.id)
        res = session.execute(statement)
        session.commit()
        self._update_repository()
        return res.scalar_one()
