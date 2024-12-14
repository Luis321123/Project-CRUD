from fastapi import APIRouter, Depends, status, Form
from typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.salsa import SalsasCreate, SalsasUpdate
from app.controllers.salsa import salsas_controller

router = APIRouter()

@router.get('/salsas', status_code=status.HTTP_200_OK)
async def get_salsas(salsas_uuid: Optional[str] = None,session: Session = Depends(get_session)):
    disciplines = await salsas_controller.get_salsas(db=session,uuid=salsas_uuid)
    return disciplines

@router.post('/salsas', status_code=status.HTTP_201_CREATED)
async def create_salsas(data: SalsasCreate = Form(...), session: Session = Depends(get_session)):
    create = await salsas_controller.create_salsas(data=data, session=session)
    return create

@router.put('/salsas', status_code=status.HTTP_200_OK)
async def update_salsas(salsas_uuid: str, data:SalsasUpdate=Form(...), session: Session = Depends(get_session)):
    update = await salsas_controller.update_salsas(data=data, salsas_uuid=salsas_uuid, session=session)
    return update

@router.delete('/salsas',status_code=status.HTTP_200_OK)
async def delete_salsas(salsas_uuid: str, session: Session = Depends(get_session)):
    await salsas_controller.delete_salsas(salsas_uuid=salsas_uuid, session=session)
    return JSONResponse({'message': 'Your comida has been deleted successfully'})