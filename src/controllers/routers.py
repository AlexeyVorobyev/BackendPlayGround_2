from src.controllers.region.controller import router as router_region
from src.swagger.swagger import router as router_swagger

all_routers = [
    router_region,
    router_swagger
]
