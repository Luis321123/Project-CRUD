from sqlalchemy.orm import Session
from fastapi import HTTPException 

from app.schemas.comida import ComidasCreate,ComidasUpdate
from app.services.base import CRUDBase
from app.models.Comida import Comida
from app.responses.comida import comida_response_create
class ComidaController(CRUDBase[Comida, ComidasCreate, ComidasUpdate]):
    async def get_comida(self, db:Session, uuid: str = None):
        if uuid:
            comida_uuid = db.query(self.model).filter(self.model.uuid == uuid).filter(self.model.deleted_at == None).first()
            if not comida_uuid:
                    raise HTTPException(status_code=404, detail="uuid of management_area not found.")
            return comida_uuid
        else:
            return db.query(self.model).filter(self.model.deleted_at == None).order_by(self.model.name.asc()).all()

    async def create_comida(self, data: ComidasCreate, session: Session): 
        try:
            comida_current = self.create(db=session, obj_in=data)
            return comida_response_create(comida_current)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error: {str(e)}")
    
    async def update_comida(self, data: ComidasUpdate, user_uuid: str, session: Session):
        try:
            comida_current = await self.get_comida(db=session, uuid=user_uuid)
            if not comida_current:
                raise HTTPException(status_code=404, detail="uuid of user not found.")
            
            comida_update=self.update(db=session, db_obj=comida_current, obj_in=data) 
            return comida_update
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")
    
    async def delete_comida(self, comida_uuid:str, session: Session):
        try:
            self.get(session, comida_uuid)
            self.remove(db=session, uuid=comida_uuid)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Hay un error:{str(e)}")

comida_controller=ComidaController(Comida)