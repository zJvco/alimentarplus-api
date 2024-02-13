from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils import generate_uuid


class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    situation = Column(String(255))
    id_supermarket = Column(Integer, ForeignKey("supermarkets.id"), nullable=False)
    id_ong = Column(Integer, ForeignKey("ongs.id"), nullable=False)
    id_product = Column(Integer, ForeignKey("products.id"), nullable=False)
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    supermarket = relationship("Supermarket", back_populates="donations", lazy='selectin')
    ong = relationship("Ong", back_populates="donations", lazy='selectin')
    product = relationship("Product", back_populates="donation", lazy='selectin', uselist=False)

    def __repr__(self) -> str:
        return "<Donation %s>" % self.id