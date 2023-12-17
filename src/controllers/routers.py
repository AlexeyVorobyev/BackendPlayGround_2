from src.controllers.region.controller import router as router_region
from src.swagger.swagger import router as router_swagger
from src.controllers.sector.controller import router as router_sector
from src.controllers.measure.controller import router as router_measure
from src.controllers.parameter.controller import router as router_parameter

all_routers = [
    router_region,
    router_sector,
    router_measure,
    router_parameter,
    router_swagger
]
