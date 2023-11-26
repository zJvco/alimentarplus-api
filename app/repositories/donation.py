from abc import ABC, abstractmethod
from sqlalchemy import select

from app.database import AsyncSessionLocal
from app.schemas.donation import DonationIn
from app.models.donations import Donation
from app.models.supermarkets import Supermarket
from app.models.ongs import Ong
from app.models.products import Product
from app.repositories.supermarket import SupermarketRepository
from app.repositories.ong import OngRepository
from app.repositories.product import ProductRepository


class DonationRepository(ABC):

    @abstractmethod
    async def get_all():
        async with AsyncSessionLocal() as session:
            query = select(Donation)
            result = await session.execute(query)

        return result.scalars().fetchall()

    @abstractmethod
    async def get_by_id(id: int):
        async with AsyncSessionLocal() as session:
            query = select(Donation).where(Donation.id == id)
            result = await session.execute(query)

        return result.scalar()
    
    @abstractmethod
    async def get_all_donations_by_supermarket_id(supermarket_id: int):
        async with AsyncSessionLocal() as session:
            query = select(Donation).where(Supermarket.id == supermarket_id)
            result = await session.execute(query)

        return result.scalars().fetchall()
    
    @abstractmethod
    async def get_all_donations_by_ong_id(ong_id: int):
        async with AsyncSessionLocal() as session:
            query = select(Donation).where(Ong.id == ong_id)
            result = await session.execute(query)

        return result.scalars().fetchall()
    
    @abstractmethod
    async def add(donation_data: DonationIn):
        async with AsyncSessionLocal() as session:
            donation = Donation(
                situation = donation_data.situation,
                id_supermarket=donation_data.id_supermarket,
                id_ong=donation_data.id_ong,
                id_product=donation_data.id_product
            )

            session.add(donation)
            await session.commit()
            await session.refresh(donation)

        return donation
    