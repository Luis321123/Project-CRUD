from fastapi import APIRouter, Depends, status, Form
from typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.dulces import DulcesCreate, DulcesUpdate
from app.controllers.dulce import dulce_controller
router = APIRouter()

@router.get('/dulce', status_code=status.HTTP_200_OK)
async def get_dulce(dulce_uuid: Optional[str] = None,session: Session = Depends(get_session)):
    disciplines = await dulce_controller.get_dulce(db=session,uuid=dulce_uuid)
    return disciplines

@router.post('/dulce', status_code=status.HTTP_201_CREATED)
async def create_dulce(data: DulcesCreate = Form(...), session: Session = Depends(get_session)):
    bebida = await dulce_controller.create_dulces(data=data, session=session)
    return bebida

@router.put('/dulce', status_code=status.HTTP_200_OK)
async def update_dulce(dulce_uuid: str, data:DulcesUpdate=Form(...), session: Session = Depends(get_session)):
    update = await dulce_controller.update_dulces(data=data, dulce_uuid=dulce_uuid, session=session)
    return update

@router.delete('/dulce',status_code=status.HTTP_200_OK)
async def delete_dulce(dulce_uuid: str, session: Session = Depends(get_session)):
    await dulce_controller.delete_dulces(dulce_uuid=dulce_uuid, session=session)
    return JSONResponse({'message': 'Your Dulce has been deleted successfully'})