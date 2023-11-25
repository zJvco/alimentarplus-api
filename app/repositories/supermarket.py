from abc import ABC, abstractmethod
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from typing import List

from app.database import AsyncSessionLocal
from app.models.supermarkets import Supermarket
from app.schemas.supermarket import SupermarketIn
from app.models.users import User
from app.schemas.user import UserIn
from app.models.addresses import Address
from app.schemas.address import AddressIn
from app.models.plans import Plan
from app.models.donations import Donation
from app.models.products import Product
from app.repositories.address import AddressRepository


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
    async def add(supermarket: SupermarketIn, user: UserIn, plan: Plan = None):
        async with AsyncSessionLocal() as session:
            supermarket = Supermarket(
                name=supermarket.name,
                business_name=supermarket.business_name,
                state_registration=supermarket.state_registration,
                phone_number=supermarket.phone_number,
                cnpj=supermarket.cnpj,
                address=supermarket.address
            )
            supermarket.users.append(user)

            session.add(supermarket)
            await session.commit()
            await session.refresh(supermarket)

        return supermarket
    
    @abstractmethod
    async def get_all_products(id_supermarket: int) -> List:
        async with AsyncSessionLocal() as session:
            query = select(Product).where(Product.id_supermarket == id_supermarket)
            result = await session.execute(query)

            products = result.scalar().products
        return products
    
    @abstractmethod
    async def get_all_donations(id_supermarket: int) -> List:
        async with AsyncSessionLocal() as session:
            query = select(Donation).where(Donation.id_supermarket == id_supermarket)
            result = await session.execute(query)

            donations = result.scalar().donations
        return donations
    
    @abstractmethod
    async def update(supermarket: SupermarketIn):
        async with AsyncSessionLocal() as session:
            update_supermarket = update(Supermarket).where(Supermarket.cnpj == supermarket.cnpj).values(
                name=supermarket.name,
                business_name=supermarket.business_name,
                state_registration=supermarket.state_registration,
                phone_number=supermarket.phone_number,
                cnpj=supermarket.cnpj,
                #id_address=supermarket.
            )
            await session.execute(update_supermarket)
            await session.commit()
            return update_supermarket

    @abstractmethod
    async def update_address(supermarket: SupermarketIn):
        address = AddressRepository.get_by_supermarket(supermarket)

        async with AsyncSessionLocal() as session:
            update_supermarket = update(Supermarket).where(Supermarket.cnpj == supermarket.cnpj).values(
                id_address= address.id
            )
            await session.execute(update_supermarket)
            await session.commit()
            return update_supermarket
    
    # @abstractmethod
    # async def add_with_user(supermarket: SupermarketIn, user: UserIn, address: AddressIn, plan: PlanIn):
    #     """
    #     Esse metodo é comumente usado na rota auth, onde temos que criar um usuário, supermercado, endereço e plano na mesma requisição
    #     """
