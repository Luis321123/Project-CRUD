from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class ComidasBase(BaseModel):
    name: str  | None= None 
    coste: int = None
    status: str = None


class ComidasCreate(ComidasBase):
    pass

class ComidasUpdate(ComidasBase):
    pass

class ComidasInDb(ComidasBase):
    uuid: UUID4
    time_get: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Comidas(ComidasInDb):
    pass