from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey

from app.database import Base
from app.utils import generate_uuid


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    street = Column(String, nullable=False) # Rua
    number = Column(String, nullable=False) 
    zip_code = Column(String, nullable=False) # CEP
    neighborhood = Column(String, nullable=False) # Bairro
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    complement = Column(String)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    def __repr__(self) -> str:
        return "<Address %s>" % self.id