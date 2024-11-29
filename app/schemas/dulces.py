from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class DulcesBase(BaseModel):
    name: str  | None= None 
    coste: int = None
    status: str = None


class DulcesCreate(DulcesBase):
    pass

class DulcesUpdate(DulcesBase):
    pass

class DulcesInDb(DulcesBase):
    uuid: UUID4
    time_get: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Dulces(DulcesInDb):
    pass