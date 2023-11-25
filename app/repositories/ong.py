from abc import ABC, abstractmethod
from sqlalchemy import select, update
from typing import List

from app.database import AsyncSessionLocal
from app.models.ongs import Ong
from app.models.users import User
from app.models.addresses import Address
from app.schemas.ong import OngIn
from app.models.donations import Donation
from app.repositories.address import AddressRepository


class OngRepository(ABC):

    @abstractmethod
    async def get_all() -> List[Ong]:
        async with AsyncSessionLocal() as session:
            query = select(Ong)
            result = await session.execute(query)
        return await result.scalars().fetchall()
    
    @abstractmethod
    async def get_by_id(id: int) -> Ong:
        async with AsyncSessionLocal() as session:
            query = select(Ong).where(Ong.id == id)
            ong = await session.execute(query)
        return await ong.scalar()


    @abstractmethod
    async def add(ong: OngIn, user: User):
        async with AsyncSessionLocal() as session:
            ong = Ong(
                name=ong.name,
                business_name=ong.business_name,
                state_registration=ong.state_registration,
                phone_number=ong.phone_number,
                cnpj=ong.cnpj,
                address=ong.address
            )
            ong.users.append(user)

            session.add(ong)
            await session.commit()
            await session.refresh(ong)
        return ong
    
    @abstractmethod
    async def get_all_donations(ong_id: int) -> List:
        async with AsyncSessionLocal() as session:
            query = select(Donation).where(Donation.id_ong == ong_id)
            result = await session.execute(query)

            donations = result.scalar().all()
        return donations
    
    @abstractmethod
    async def update(ong: OngIn):
        async with AsyncSessionLocal() as session:
            update_ong = update(Ong).where(Ong.cnpj == ong.cnpj).values(
                name=ong.name,
                business_name=ong.business_name,
                state_registration=ong.state_registration,
                phone_number=ong.phone_number,
                cnpj=ong.cnpj,
                #id_address=ong.id
            )
            await session.execute(update_ong)
            await session.commit()
            return update_ong


    @abstractmethod
    async def update_address(ong: OngIn):
        address = AddressRepository.get_by_ong(ong)

        async with AsyncSessionLocal() as session:
            update_ong = update(Ong).where(Ong.cnpj == ong.cnpj).values(
                id_address= address.id
            )
            await session.execute(update_ong)
            await session.commit()
            return update_ong
        