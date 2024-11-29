from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import ARRAY
from sqlalchemy.orm import relationship

from app.models.BaseModel import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    uuid = Column(
        UUID(150), primary_key=True,  index=True, default=uuid4
    )   
    username = Column(String(255))
    role = Column(String(255))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    #Relaciones

    notifications = relationship("Notification", back_populates="users")
