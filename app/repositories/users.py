from abc import ABC, abstractmethod
from typing import List
from sqlalchemy import select, delete

from app.database import AsyncSessionLocal
from app.models.users import User
from app.utils import verify_password, generate_password_hash


class UserRepository(ABC):

    @abstractmethod
    async def get_all() -> List:
        async with AsyncSessionLocal() as session:
            query = select(User)
            result = await session.execute(query)

        return result.fetchall()
    
    @abstractmethod
    async def add(name: str, email: str, phone_number: str, cpf: str, password: str, role="A") -> None:
        async with AsyncSessionLocal() as session:
            user = User(
                name=name,
                email=email,
                phone_number=phone_number,
                cpf=cpf,
                password_hash=generate_password_hash(password)
            )

            # user.role = role

            session.add(user)
            await session.commit()
            await session.refresh(user)
            
        return user

    @abstractmethod
    async def get_by_id(id: int):
        async with AsyncSessionLocal() as session:
            query = select(User).where(User.id == id)
            user = await session.execute(query)

        return user.first()
    
    @abstractmethod
    async def delete(id: int):
        async with AsyncSessionLocal() as session:
            query = delete(User).where(User.id == id)

            await session.execute(query)
            await session.commit()
        
        return id
    
    @abstractmethod
    async def get_by_email(email: str):
        async with AsyncSessionLocal() as session:
            query = select(User).where(User.email == email)
            user = await session.execute(query)

        return user.first()