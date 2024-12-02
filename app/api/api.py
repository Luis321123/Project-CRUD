from fastapi import APIRouter, Depends
from app.api.endpoints.debug import router as router_debug
from app.api.endpoints.user import router as router_user
from app.api.endpoints.bebida import router as router_bebidas
api_router = APIRouter()

api_router.include_router(router_user, tags=["User"],
    responses={404: {"description": "Not found"}})

api_router.include_router(router_debug, tags=["Debug"],
    responses={404: {"description": "Not found"}})

api_router.include_router(router_bebidas, tags=["Bebidas"],
    responses={404: {"description": "Not found"}})