from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

from app.database import AsyncSessionLocal
from app.schemas.plan import PlanIn
from app.models.plans import Plan


class PlanRepository(ABC):

    @abstractmethod
    async def add(plan_data: PlanIn):
        async with AsyncSessionLocal() as session:
            plan = Plan(
                name=plan_data.name,
                price=plan_data.price,
                description=plan_data.description
            )

            session.add(plan)

            await session.commit()
            await session.refresh(plan)

        return plan
    
    @abstractmethod
    async def get_all():
        async with AsyncSessionLocal() as session:
            query = select(Plan)
            result = await session.execute(query)

        return result.scalars().fetchall()
    
    @abstractmethod
    async def get_by_name(name: str):
        async with AsyncSessionLocal() as session:
            query = select(Plan).where(Plan.name == name)
            result = await session.execute(query)

        return result.scalar()
    
    @abstractmethod
    async def get_by_id(id: int):
        async with AsyncSessionLocal() as session:
            query = select(Plan).where(Plan.id == id)
            result = await session.execute(query)

        return result.scalar()