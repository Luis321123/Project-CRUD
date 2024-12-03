from sqlalchemy.orm import Session
from fastapi import HTTPException 

from app.schemas.enlatados import EnlatadosCreate,EnlatadosUpdate
from app.services.base import CRUDBase
from app.models.Enlatado import Enlatado
from app.responses.enlatados import enlatados_response_create
class EnlatadoController(CRUDBase[Enlatado, EnlatadosCreate, EnlatadosUpdate]):
    async def get_enlatado(self, db:Session, uuid: str = None):
        if uuid:
            enlatados_uuid = db.query(self.model).filter(self.model.uuid == uuid).filter(self.model.deleted_at == None).first()
            if not enlatados_uuid:
                    raise HTTPException(status_code=404, detail="uuid of management_area not found.")
            return enlatados_uuid
        else:
            return db.query(self.model).filter(self.model.deleted_at == None).order_by(self.model.name.asc()).all()

    async def create_enlatado(self, data: EnlatadosCreate, session: Session): 
        try:
            enlatado_current = self.create(db=session, obj_in=data)
            return enlatados_response_create(enlatado_current)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error: {str(e)}")
    
    async def update_enlatado(self, data: EnlatadosUpdate, user_uuid: str, session: Session):
        try:
            enlatado_current = await self.get_enlatado(db=session, uuid=user_uuid)
            if not enlatado_current:
                raise HTTPException(status_code=404, detail="uuid of user not found.")
            
            enlatado_update=self.update(db=session, db_obj=enlatado_current, obj_in=data) 
            return enlatado_update
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def delete_enlatado(self, enlatado_uuid:str, session: Session):
        try:
            self.get(session, enlatado_uuid)
            self.remove(db=session, uuid=enlatado_uuid)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

enlatado_controller=EnlatadoController(Enlatado)