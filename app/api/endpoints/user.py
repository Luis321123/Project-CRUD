from fastapi import APIRouter, Depends, Form, status
from typing import Optional
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.core.database import get_session
from app.schemas.user import UserCreate, UserUpdate
from app.controllers.users import user_controller

router = APIRouter()

@router.get('/users', status_code=status.HTTP_200_OK)
async def get_users(user_uuid: Optional[str] = None,session: Session = Depends(get_session)):
    disciplines = await user_controller.get_user(db=session,uuid=user_uuid)
    return disciplines

@router.post('/users', status_code=status.HTTP_201_CREATED)
async def create_users(data: UserCreate = str, session: Session = Depends(get_session)):
    user = await user_controller.create_user(data=data, session=session)
    return user

@router.put('/user', status_code=status.HTTP_200_OK)
async def update_users(user_uuid: str, data:UserUpdate=str, session: Session = Depends(get_session)):
    update = await user_controller.update_user(data=data, user_uuid=user_uuid, session=session)
    return update

@router.delete('/user',status_code=status.HTTP_200_OK)
async def delete_users(uuid: str, session: Session = Depends(get_session)):
    await user_controller.delete_user(disciplines_uuid=uuid, session=session)
    return JSONResponse({'message': 'Your User has been deleted successfully'})