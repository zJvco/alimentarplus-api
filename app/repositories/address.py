from abc import ABC, abstractmethod

from app.models.addresses import Address
from app.database import AsyncSessionLocal


class AddressRepository(ABC):

    @abstractmethod
    async def add(street: str, number: str, zip_code: str, neighborhood: str, state: str, city: str, complement: str):
        async with AsyncSessionLocal() as session:
            address = Address(
                street=street,
                number=number,
                zip_code=zip_code,
                neighborhood=neighborhood,
                state=state,
                city=city,
                complement=complement
            )

            session.add(address)
            await session.commit()
            await session.refresh(address)

        return address

