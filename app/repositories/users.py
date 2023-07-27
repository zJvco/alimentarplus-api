from abc import ABC, abstractmethod
from typing import List
from sqlalchemy import select

from app.database import AsyncSessionLocal
from app.models.users import User


class UserRepository(ABC):

    @abstractmethod
    async def get_all() -> List:
        async with AsyncSessionLocal() as session:
            query = select(User)
            result = await session.execute(query)

            return result.fetchall()
    
    @abstractmethod
    async def create(name: str, email: str, phone_number: str, cpf: str, password: str) -> None:
        async with AsyncSessionLocal() as session:
            user = User(
                name=name,
                email=email,
                phone_number=phone_number,
                cpf=cpf,
                password_hash=password
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            
            return user
