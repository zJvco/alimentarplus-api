from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

from app.database import AsyncSessionLocal
from app.models.supermarkets import Supermarket
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
    async def add(name: str, business_name: str, state_registration: str, phone_number: str, cnpj: str, address: Address, user: User, plan: Plan = None):
        async with AsyncSessionLocal() as session:
            supermarket = Supermarket(
                name=name,
                business_name=business_name,
                state_registration=state_registration,
                phone_number=phone_number,
                cnpj=cnpj,
                address=address
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