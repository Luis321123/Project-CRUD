from fastapi import APIRouter, Depends, Form, status, Form
from typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.carnes import Carnescreate, CarnesUpdate
from app.controllers.carnes import carne_controller

router = APIRouter()

@router.get('/carne', status_code=status.HTTP_200_OK)
async def get_carne(carne_uuid: Optional[str] = None,session: Session = Depends(get_session)):
    get = await carne_controller.get_carne(db=session,uuid=carne_uuid)
    return get

@router.post('/carne', status_code=status.HTTP_201_CREATED)
async def create_carne(data: Carnescreate = Form(...), session: Session = Depends(get_session)):
    create = await carne_controller.create_carne(data=data, session=session)
    return create

@router.put('/carne', status_code=status.HTTP_200_OK)
async def update_carne(carne_uuid: str, data:CarnesUpdate=Form(...), session: Session = Depends(get_session)):
    update = await carne_controller.update_carne(data=data, carne_uui=carne_uuid, session=session)
    return update

@router.delete('/carne',status_code=status.HTTP_200_OK)
async def delete_carne(carne_uuid: str, session: Session = Depends(get_session)):
    await carne_controller.delete_carne(carne_uuid=carne_uuid, session=session)
    return JSONResponse({'message': 'Your Carne has been deleted successfully'})
