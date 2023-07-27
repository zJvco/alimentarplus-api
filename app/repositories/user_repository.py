from abc import ABC, abstractmethod

from app.database import AsyncSessionLocal


class UserRepository(ABC):

    @abstractmethod
    async def get_all():
        async with AsyncSessionLocal() as session:
            result = await session.execute("SELECT * FROM users")

            return result.scalars().all()
