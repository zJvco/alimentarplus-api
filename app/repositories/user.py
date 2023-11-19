from abc import ABC, abstractmethod
from typing import List
from sqlalchemy import select, delete

from app.database import AsyncSessionLocal
from app.models.users import User
from app.schemas.user import UserIn
from app.utils import generate_password_hash


class UserRepository(ABC):

    @abstractmethod
    async def get_all() -> List[User]:
        async with AsyncSessionLocal() as session:
            query = select(User)
            result = await session.execute(query)

        return result.scalars().fetchall()
    
    @abstractmethod
    async def add(user: UserIn, role="A") -> User:
        async with AsyncSessionLocal() as session:
            user = User(
                name=user.name,
                email=user.email,
                phone_number=user.phone_number,
                cpf=user.cpf,
                password_hash=generate_password_hash(user.password)
            )

            # user.role = role

            session.add(user)
            await session.commit()
            await session.refresh(user)
            
        return user

    @abstractmethod
    async def get_by_id(id: int) -> User:
        async with AsyncSessionLocal() as session:
            query = select(User).where(User.id == id)
            user = await session.execute(query)

        return user.scalar()
    
    @abstractmethod
    async def delete(id: int) -> int:
        async with AsyncSessionLocal() as session:
            query = delete(User).where(User.id == id)

            await session.execute(query)
            await session.commit()
        
        return id
    
    @abstractmethod
    async def get_by_email(email: str) -> User:
        async with AsyncSessionLocal() as session:
            query = select(User).where(User.email == email)
            user = await session.execute(query)

        return user.scalar()