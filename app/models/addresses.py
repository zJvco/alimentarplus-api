from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(255), nullable=False) # Rua
    number = Column(String(255), nullable=False) 
    zip_code = Column(String(8), nullable=False) # CEP
    neighborhood = Column(String(255), nullable=False) # Bairro
    state = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    complement = Column(String(255))
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    supermarket = relationship("Supermarket", back_populates="address", lazy='selectin')
    ong = relationship("Ong", back_populates="address", lazy='selectin')

    def __repr__(self) -> str:
        return "<Address %s>" % self.id