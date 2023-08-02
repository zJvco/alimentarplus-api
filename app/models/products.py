from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database import Base
from app.utils import generate_uuid


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    name = Column(String, nullable=False, unique=True)
    brand = Column(String, nullable=False)
    description = Column(String)
    unit_weight_grams = Column(String, nullable=False)
    total_weight_grams = Column(String, nullable=False)
    quantity_units = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    expiration_date = Column(DateTime)
    url_product_img = Column(String, nullable=False)
    url_expiration_date_img = Column(String, nullable=False)
    id_supermarket = Column(Integer, ForeignKey("supermarkets.id"), nullable=False)
    id_category = Column(Integer, ForeignKey("categories.id"))
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    supermarket = relationship("Supermarket", backref="products")
    category = relationship("Category", backref="products")

    def __repr__(self) -> str:
        return "<Product %s>" % self.id