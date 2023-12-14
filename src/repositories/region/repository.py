from src.models.region.model import RegionModel
from src.utils.classes.BaseRepository import BaseRepository
from src.SQLAlchemy.connection import PostgreAlchemyConnection
from src.utils.classes.config import Config
from sqlalchemy import select
from src.utils.decorators.singleton import singleton


@singleton
class RegionRepository(BaseRepository):
    def __init__(self):
        self._collection: list[RegionModel] = []
        self._update_repository()

    def _update_repository(self):
        try:
            session = PostgreAlchemyConnection(Config()).session_maker()
            statement = select(RegionModel)
            result = session.execute(statement)
            self._collection = [item[0] for item in result.all()]
        except ValueError:
            print(ValueError)

    def get_all(self, page: int = 0, per_page: int = 8) -> list[RegionModel]:
        return self._collection
        pass

    def get_by_id(self, id_arg: str) -> RegionModel | None:
        pass

    def create(self, model_instance: RegionModel) -> bool:
        pass

    def replace(self, id_arg: str, model_instance: RegionModel) -> bool:
        pass

    def update(self, id_arg: str, model_instance: RegionModel) -> bool:
        pass

    def delete_by_id(self, id_arg: str) -> bool:
        pass


print(RegionRepository)
print(RegionRepository().get_all())
