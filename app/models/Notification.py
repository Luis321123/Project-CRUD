from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ARRAY
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel

class Notification(BaseModel):
    __tablename__ = 'notifications'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )   
    name = Column(String(255))
    description = Column(String(255))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    #Relaciones

    users = relationship("User", back_populates="notifications")
