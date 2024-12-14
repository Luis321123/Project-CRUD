from fastapi import APIRouter
from app.api.endpoints.debug import router as router_debug
from app.api.endpoints.user import router as router_user
from app.api.endpoints.bebida import router as router_bebidas
from app.api.endpoints.comida import router as router_comidas
from app.api.endpoints.enlatado import router as router_enlatados
from app.api.endpoints.carne import router as router_carnes
from app.api.endpoints.dulce import router as router_dulces
from app.api.endpoints.salsas import router as router_salsas
api_router = APIRouter()

api_router.include_router(router_user, tags=["User"],
    responses={404: {"description": "Not found"}})
api_router.include_router(router_salsas, tags=["Salsas"],
    responses={404: {"description": "Not found"}})
api_router.include_router(router_bebidas, tags=["Bebidas"],
    responses={404: {"description": "Not found"}})
api_router.include_router(router_comidas, tags=["Comidas"],
    responses={404: {"description": "Not found"}})
api_router.include_router(router_enlatados, tags=["Enlatados"],
    responses={404: {"description": "Not found"}})
api_router.include_router(router_carnes, tags=["Carnes"], 
    responses={404: {"description": "Not found"}})
api_router.include_router(router_dulces, tags=["Dulces"],
    responses={404: {"description": "Not found"}})
api_router.include_router(router_debug, tags=["Debug"],
    responses={404: {"description": "Not found"}})