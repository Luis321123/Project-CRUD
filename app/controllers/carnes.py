from sqlalchemy.orm import Session
from fastapi import HTTPException 

from app.schemas.carnes import Carnescreate, CarnesUpdate
from app.services.base import CRUDBase
from app.models.Carne import Carne
from app.responses.carne import carne_response_create
class CarneController(CRUDBase[Carne, Carnescreate, CarnesUpdate]):
    async def get_carne(self, db:Session, uuid: str = None):
        if uuid:
            carnes_uuid = db.query(self.model).filter(self.model.uuid == uuid).filter(self.model.deleted_at == None).first()
            if not carnes_uuid:
                    raise HTTPException(status_code=404, detail="uuid of management_area not found.")
            return carnes_uuid
        else:
            return db.query(self.model).filter(self.model.deleted_at == None).order_by(self.model.name.asc()).all()

    async def create_carne(self, data: Carnescreate, session: Session): 
        try:
            carnes_current = self.create(db=session, obj_in=data)
            return carne_response_create(carnes_current)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error: {str(e)}")
    
    async def update_carne(self, data: CarnesUpdate, carne_uuid: str, session: Session):
        try:
            carne_current = await self.get_carne(db=session, uuid=carne_uuid)
            if not carne_current:
                raise HTTPException(status_code=404, detail="uuid of user not found.")
            
            carne_update=self.update(db=session, db_obj=carne_current, obj_in=data) 
            return carne_update
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def delete_carne(self, carne_uuid:str, session: Session):
        try:
            self.get(session, carne_uuid)
            self.remove(db=session, uuid=carne_uuid)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

carne_controller=CarneController(Carne)