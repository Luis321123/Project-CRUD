from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class UserBase(BaseModel):
    username: str  | None= None 
    role: str = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDb(UserBase):
    uuid: UUID4
    created_at: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class User(UserInDb):
    pass