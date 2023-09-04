from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

from app.database import AsyncSessionLocal
from app.models.supermarkets import Supermarket
from app.schemas.supermarket import Supermarket as Supermarket_schema
from app.models.users import User
from app.models.addresses import Address
from app.models.plans import Plan


class SupermarketRepository(ABC):

    @abstractmethod
    async def get_all() -> List[Supermarket]:
        async with AsyncSessionLocal() as session:
            query = select(Supermarket)
            result = await session.execute(query)
        
        return result.scalars().fetchall()
    
    @abstractmethod
    async def get_by_id(id: int) -> Supermarket:
        async with AsyncSessionLocal() as session:
            query = select(Supermarket).where(Supermarket.id == id)
            supermarket = await session.execute(query)
        
        return supermarket.scalar()

    @abstractmethod
    async def add(supermarket: Supermarket_schema, user: User, plan: Plan = None):
        async with AsyncSessionLocal() as session:
            supermarket = Supermarket(
                name=Supermarket_schema.name,
                business_name=Supermarket_schema.business_name,
                state_registration=Supermarket_schema.state_registration,
                phone_number=Supermarket_schema.phone_number,
                cnpj=Supermarket_schema.cnpj,
                address=Supermarket_schema.address
            )

            supermarket.users.append(user)

            session.add(supermarket)
            await session.commit()
            await session.refresh(supermarket)

        return supermarket
    
    @abstractmethod
    async def get_all_products(supermarket_id: int) -> List:
        async with AsyncSessionLocal() as session:
            query = select(Supermarket)
            result = await session.execute(query)

            products = result.scalar().products

        return products
