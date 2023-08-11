from abc import ABC, abstractmethod

from app.database import AsyncSessionLocal
from app.models.ongs import Ong
from app.models.users import User
from app.models.addresses import Address


class OngRepository(ABC):

    @abstractmethod
    async def add(name: str, business_name: str, state_registration: str, phone_number: str, cnpj: str, address: Address, user: User):
        async with AsyncSessionLocal() as session:
            ong = Ong(
                name=name,
                business_name=business_name,
                state_registration=state_registration,
                phone_number=phone_number,
                cnpj=cnpj,
                address=address
            )

            ong.users.append(user)

            session.add(ong)
            await session.commit()
            await session.refresh(ong)

        return ong