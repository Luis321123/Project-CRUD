from uuid import uuid4
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
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
    user_uuid = Column(UUID(150),ForeignKey('users.uuid'), nullable=False)
    enlatado_uuid = Column(UUID(150),ForeignKey('enlatados.uuid'), nullable=False)
    dulce_uuid = Column(UUID(150),ForeignKey('dulces.uuid'), nullable=False)
    bebida_uuid = Column(UUID(150),ForeignKey('bebidas.uuid'), nullable=False)
    carne_uuid = Column(UUID(150),ForeignKey('carnes.uuid'), nullable=False)
    comida_uuid = Column(UUID(150),ForeignKey('comidas.uuid'), nullable=False)
    salsa_uuid = Column(UUID(150),ForeignKey('salsas.uuid'), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True, default=None)

    #Relaciones

    users = relationship("User", back_populates="notifications", uselist=False)
    enlatado = relationship("Enlatado", back_populates="notifications", uselist=False)
    dulce = relationship("Dulce", back_populates="notifications", uselist=False)
    bebida = relationship("Bebida", back_populates="notifications", uselist=False)
    carne = relationship("Carne", back_populates="notifications", uselist=False)
    comida = relationship("Comida", back_populates="notifications", uselist=False)
    salsa = relationship("Salsa", back_populates="notifications", uselist=False)
