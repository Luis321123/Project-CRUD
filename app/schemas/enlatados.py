from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class Enlatadosbase(BaseModel):
    name: str  | None= None 
    coste: int = None
    status: str = None


class EnlatadosCreate(Enlatadosbase):
    pass

class EnlatadosUpdate(Enlatadosbase):
    pass

class EnlatadosInDb(Enlatadosbase):
    uuid: UUID4
    time_get: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Enlatados(EnlatadosInDb):
    pass