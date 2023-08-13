from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String(11), unique=True, nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    # id_role = Column(Integer, ForeignKey("roles.id"), nullable=False)
    id_supermarket = Column(Integer, ForeignKey("supermarkets.id"))
    id_ong = Column(Integer, ForeignKey("ongs.id"))
    created_date = Column(DateTime, default=func.now())
    updated_date = Column(DateTime, onupdate=func.now())

    # role = relationship("Role", back_populates="users", lazy='selectin')
    supermarket = relationship("Supermarket", back_populates="users", lazy='selectin')
    ong = relationship("Ong", back_populates="users", lazy='selectin')

    def __repr__(self) -> str:
        return "<User %s>" % self.id