from fastapi import APIRouter, Depends, status
from typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.enlatados import EnlatadosCreate,EnlatadosUpdate
from app.controllers.enlatados import enlatado_controller

router = APIRouter()

@router.get('/enlatado', status_code=status.HTTP_200_OK)
async def get_enlatado(enlatado_uuid: Optional[str] = None,session: Session = Depends(get_session)):
    disciplines = await enlatado_controller.get_enlatado(db=session,uuid=enlatado_uuid)
    return disciplines

@router.post('/enlatado', status_code=status.HTTP_201_CREATED)
async def create_enlatado(data: EnlatadosCreate = str, session: Session = Depends(get_session)):
    bebida = await enlatado_controller.create_enlatado(data=data, session=session)
    return bebida

@router.put('/enlatado', status_code=status.HTTP_200_OK)
async def update_enlatado(enlatado_uuid: str, data:EnlatadosUpdate=str, session: Session = Depends(get_session)):
    update = await enlatado_controller.update_enlatado(data=data, enlatado_uuid=enlatado_uuid, session=session)
    return update

@router.delete('/enlatado',status_code=status.HTTP_200_OK)
async def delete_enlatado(uuid: str, session: Session = Depends(get_session)):
    await enlatado_controller.delete_enlatado(disciplines_uuid=uuid, session=session)
    return JSONResponse({'message': 'Your comida has been deleted successfully'})