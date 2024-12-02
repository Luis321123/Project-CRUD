from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.user import UserCreate, UserUpdate
from app.services.base import CRUDBase
from app.models.User import User

class UserController(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_user(self, db:Session, uuid: str = None):
        if uuid:
            user_uuid = db.query(self.model).filter(self.model.uuid == uuid).filter(self.model.deleted_at == None).first()
            if not user_uuid:
                    raise HTTPException(status_code=404, detail="uuid of management_area not found.")
            return user_uuid
        else:
            return db.query(self.model).filter(self.model.deleted_at == None).order_by(self.model.username.asc()).all()

    async def create_user(self, data: UserCreate, session: Session):
        try:
            user_current = self.create(db=session, obj_in=data)
            return user_current
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def update_user(self, data: UserUpdate, user_uuid: str, session: Session):
        try:
            user_current = await self.get_user(db=session, uuid=user_uuid)
            if not user_current:
                raise HTTPException(status_code=404, detail="uuid of user not found.")
            
            user_update=self.update(db=session, db_obj=user_current, obj_in=data)
            return user_update
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def delete_user(self, user_uuid:str, session: Session):
        try:
            db_obj = {"active": False}
            user_currentt = self.get(session, user_uuid)
            self.update(db=session, db_obj=user_currentt, obj_in=db_obj)
            self.remove(db=session, uuid=user_uuid)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

user_controller=UserController(User)