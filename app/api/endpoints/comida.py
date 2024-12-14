from fastapi import APIRouter, Depends, status, Form
from typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.comida import ComidasCreate,ComidasUpdate
from app.controllers.comida import comida_controller

router = APIRouter()

@router.get('/comida', status_code=status.HTTP_200_OK)
async def get_comida(comida_uuid: Optional[str] = None,session: Session = Depends(get_session)):
    disciplines = await comida_controller.get_comida(db=session,uuid=comida_uuid)
    return disciplines

@router.post('/comida', status_code=status.HTTP_201_CREATED)
async def create_comida(data: ComidasCreate = Form(...), session: Session = Depends(get_session)):
    bebida = await comida_controller.create_comida(data=data, session=session)
    return bebida

@router.put('/comida', status_code=status.HTTP_200_OK)
async def update_comida(comida_uuid: str, data:ComidasUpdate= Form(...), session: Session = Depends(get_session)):
    update = await comida_controller.update_comida(data=data, comida_uuid=comida_uuid, session=session)
    return update

@router.delete('/comida',status_code=status.HTTP_200_OK)
async def delete_comida(comida_uuid: str, session: Session = Depends(get_session)):
    await comida_controller.delete_comida(comida_uuid=comida_uuid, session=session)
    return JSONResponse({'message': 'Your comida has been deleted successfully'})