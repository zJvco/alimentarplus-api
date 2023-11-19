from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from typing import List

from app.database import AsyncSessionLocal
from app.models.supermarkets import Supermarket
from app.schemas.supermarket import SupermarketIn
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
    async def add(supermarket: SupermarketIn, user: User, address: Address, plan: Plan = None):
        async with AsyncSessionLocal() as session:
            supermarket = Supermarket(
                name=supermarket.name,
                business_name=supermarket.business_name,
                state_registration=supermarket.state_registration,
                phone_number=supermarket.phone_number,
                cnpj=supermarket.cnpj,
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
    
    # @abstractmethod
    # async def add_with_user(supermarket: SupermarketIn, user: UserIn, address: AddressIn, plan: PlanIn):
    #     """
    #     Esse metodo é comumente usado na rota auth, onde temos que criar um usuário, supermercado, endereço e plano na mesma requisição
    #     """
