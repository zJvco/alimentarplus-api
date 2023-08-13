from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Supermarket(Base):
    __tablename__ = "supermarkets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True) # Nome Fantasia
    business_name = Column(String, nullable=False, unique=True) # Razão Social
    state_registration = Column(String, nullable=False, unique=True) # Inscrição Estadual
    phone_number = Column(String(11), nullable=False, unique=True)
    cnpj = Column(String(14), nullable=False, unique=True)
    # id_plan = Column(Integer, ForeignKey("plans.id"), nullable=False)
    id_address = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    # plan = relationship("Plan", back_populates="supermarkets, lazy='selectin'")
    address = relationship("Address", back_populates="supermarket", lazy='selectin', uselist=False)
    donations = relationship("Donation", back_populates="supermarket", lazy='selectin')
    users = relationship("User", back_populates="supermarket", lazy='selectin')
    products = relationship("Product", back_populates="supermarket", lazy='selectin')

    def __repr__(self) -> str:
        return "<Supermarket %s>" % self.id