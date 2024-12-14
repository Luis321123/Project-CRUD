from sqlalchemy.orm import Session
from fastapi import HTTPException 
from app.schemas.dulces import DulcesCreate, DulcesUpdate
from app.services.base import CRUDBase
from app.models.Dulce import Dulce
from app.responses.dulce import dulce_response_create
class DulceController(CRUDBase[Dulce, DulcesCreate, DulcesUpdate]):
    async def get_dulce(self, db:Session, uuid: str = None):
        if uuid:
            dulces_uuid = db.query(self.model).filter(self.model.uuid == uuid).filter(self.model.deleted_at == None).first()
            if not dulces_uuid:
                    raise HTTPException(status_code=404, detail="uuid of Dulce not found.")
            return dulces_uuid
        else:
            dulce_porsia=db.query(self.model).filter(self.model.deleted_at == None).order_by(self.model.name.asc()).all()
            if not dulce_porsia:
                raise HTTPException(status_code=404, detail="En estos momentos no tienes dulces disponibles.")
            return dulce_porsia

    async def create_dulces(self, data: DulcesCreate, session: Session): 
        try:
            dulces_current = self.create(db=session, obj_in=data)
            return dulce_response_create(dulces_current)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error: {str(e)}")
    
    async def update_dulces(self, data: DulcesUpdate, dulce_uuid: str, session: Session):
        try:
            dulce_current = await self.get_dulce(db=session, uuid=dulce_uuid)
            if not dulce_current:
                raise HTTPException(status_code=404, detail="uuid of user not found.")
            
            dulce_update=self.update(db=session, db_obj=dulce_current, obj_in=data) 
            return dulce_update
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def delete_dulces(self, dulce_uuid:str, session: Session):
        try:
            self.get(session, dulce_uuid)
            self.remove(db=session, uuid=dulce_uuid)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

dulce_controller=DulceController(Dulce)