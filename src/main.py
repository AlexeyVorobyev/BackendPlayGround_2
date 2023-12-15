import uvicorn
from fastapi import FastAPI

from src.controllers.routers import all_routers

app = FastAPI(
    title="Сервис для хранения экономических данных"
)


for router in all_routers:
    app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)