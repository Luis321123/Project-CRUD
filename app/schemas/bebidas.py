from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class BebidasBase(BaseModel):
    name: str  | None= None 
    coste: int = None
    status: str = None


class BebidasCreate(BebidasBase):
    pass

class BebidasUpdate(BebidasBase):
    pass

class BebidasInDb(BebidasBase):
    uuid: UUID4
    time_get: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Bebidas(BebidasInDb):
    pass