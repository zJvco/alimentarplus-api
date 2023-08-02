from abc import ABC, abstractmethod

from app.database import AsyncSessionLocal
from app.models.supermarkets import Supermarket


class SupermarketRepository(ABC):

    @abstractmethod
    async def add(name: str, business_name: str, state_registration: str, phone_number: str, cnpj: str, address, plan=None):
        async with AsyncSessionLocal() as session:
            supermarket = Supermarket(
                name=name,
                business_name=business_name,
                state_registration=state_registration,
                phone_number=phone_number,
                cnpj=cnpj,
                address=address
            )

            session.add(supermarket)
            await session.commit()
            await session.refresh(supermarket)

        return supermarket