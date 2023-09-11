from abc import ABC, abstractmethod
from sqlalchemy import select, delete

from app.models.addresses import Address
from app.schemas.address import AddressIn
from app.database import AsyncSessionLocal


class AddressRepository(ABC):

    @abstractmethod
    async def add(address: AddressIn) -> Address:
        async with AsyncSessionLocal() as session:
            address = Address(
                street=address.street,
                number=address.number,
                zip_code=address.zip_code,
                neighborhood=address.neighborhood,
                state=address.state,
                city=address.city,
                complement=address.complement
            )

            session.add(address)
            await session.commit()
            await session.refresh(address)

        return address

    @abstractmethod
    async def delete(id: int) -> int:
        async with AsyncSessionLocal() as session:
            query = delete(Address).where(Address.id == id)

            await session.execute(query)
            await session.commit()
        
        return id