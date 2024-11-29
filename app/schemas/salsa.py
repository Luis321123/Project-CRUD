from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class SalsasBase(BaseModel):
    name: str  | None= None 
    coste: int = None
    status: str = None


class SalsasCreate(SalsasBase):
    pass

class SalsasUpdate(SalsasBase):
    pass

class SalsasInDb(SalsasBase):
    uuid: UUID4
    time_get: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Salsas(SalsasInDb):
    pass