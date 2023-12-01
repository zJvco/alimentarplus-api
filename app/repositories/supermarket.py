from abc import ABC, abstractmethod
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from typing import List

from app.database import AsyncSessionLocal
from app.models.supermarkets import Supermarket
from app.schemas.supermarket import SupermarketIn
from app.models.users import User
from app.models.addresses import Address
from app.models.plans import Plan
from app.schemas.plan import PlanIn


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
            result = await session.execute(query)
        
        return result.scalar()

    @abstractmethod
    async def add(supermarket: SupermarketIn, user: User, address: Address, plan: Plan):
        async with AsyncSessionLocal() as session:
            supermarket = Supermarket(
                name=supermarket.name,
                business_name=supermarket.business_name,
                state_registration=supermarket.state_registration,
                phone_number=supermarket.phone_number,
                cnpj=supermarket.cnpj,
                address=address
            )

            supermarket.address = address
            supermarket.plan = plan
            supermarket.users.append(user)

            session.add(supermarket)

            await session.commit()
            await session.refresh(supermarket)

        return supermarket
    
    @abstractmethod
    async def update(id: int, supermarket_data: SupermarketIn):
        async with AsyncSessionLocal() as session:
            query = update(Supermarket).where(Supermarket.id == id).values(dict(supermarket_data))
            await session.execute(query)
            await session.commit()

        return id
    
    @abstractmethod
    async def update_plan(supermarket_id: int, plan_id: int):
        async with AsyncSessionLocal() as session:
            query = update(Supermarket)\
                .where(Supermarket.id == supermarket_id)\
                .values(id_plan=plan_id)
            
            await session.execute(query)
            await session.commit()

        return plan_id