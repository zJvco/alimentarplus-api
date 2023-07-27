import uuid
from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(36), nullable=False, unique=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    # id_role = 
    # id_supermarket = 
    # id_ong =

    def __repr__(self) -> str:
        return "<User %s>" % self.id