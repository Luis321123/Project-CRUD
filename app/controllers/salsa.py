from sqlalchemy.orm import Session
from fastapi import HTTPException 
from app.schemas.salsa import SalsasCreate, SalsasUpdate
from app.services.base import CRUDBase
from app.models.Salsa import Salsa
from app.responses.salsas import salsas_response_create
class SalsasController(CRUDBase[Salsa, SalsasCreate, SalsasUpdate]):
    async def get_salsas(self, db:Session, uuid: str = None):
        if uuid:
            salsas_uuid = db.query(self.model).filter(self.model.uuid == uuid).filter(self.model.deleted_at == None).first()
            if not salsas_uuid:
                    raise HTTPException(status_code=404, detail="uuid of Dulce not found.")
            return salsas_uuid
        else:
            salsas_porsia=db.query(self.model).filter(self.model.deleted_at == None).order_by(self.model.name.asc()).all()
            if not salsas_porsia:
                raise HTTPException(status_code=404, detail="En estos momentos no tienes salsas disponibles.")
            return salsas_porsia

    async def create_salsas(self, data: SalsasCreate, session: Session): 
        try:
            salsas_current = self.create(db=session, obj_in=data)
            return salsas_response_create(salsas_current)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error: {str(e)}")
    
    async def update_salsas(self, data: SalsasUpdate, salsas_uuid: str, session: Session):
        try:
            salsas_current = await self.get_salsas(db=session, uuid=salsas_uuid)
            if not salsas_current:
                raise HTTPException(status_code=404, detail="uuid of user not found.")
            
            salsas_update=self.update(db=session, db_obj=salsas_current, obj_in=data) 
            return salsas_update
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def delete_salsas(self, salsas_uuid:str, session: Session):
        try:
            self.get(session, salsas_uuid)
            self.remove(db=session, uuid=salsas_uuid)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

salsas_controller=SalsasController(Salsa)