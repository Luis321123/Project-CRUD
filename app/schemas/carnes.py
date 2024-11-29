from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class CarnesBase(BaseModel):
    name: str  | None= None 
    coste: int = None
    status: str = None


class Carnescreate(CarnesBase):
    pass

class CarnesUpdate(CarnesBase):
    pass

class CarnesIndb(CarnesBase):
    uuid: UUID4
    time_get: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Carnes(CarnesIndb):
    pass