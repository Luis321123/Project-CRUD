from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel


class NotificationBase(BaseModel):
    name: str  | None= None 
    description: str = None
    status: str = None

class NotificationCreate(NotificationBase):
    pass

class NotificationUpdate(NotificationBase):
    pass

class NotificationInDb(NotificationBase):
    uuid: UUID4
    created_at: datetime = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class Notification(NotificationInDb):
    pass