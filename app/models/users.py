from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from app.database import Base
from app.utils import generate_uuid


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=lambda: generate_uuid())
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    # id_role = 
    # id_supermarket = 
    # id_ong =
    created_date = Column(DateTime, nullable=False, default=func.now())
    updated_date = Column(DateTime, nullable=False, onupdate=func.now())

    def __repr__(self) -> str:
        return "<User %s>" % self.id