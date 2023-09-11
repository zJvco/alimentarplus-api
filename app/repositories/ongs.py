from abc import ABC, abstractmethod

from app.database import AsyncSessionLocal
from app.models.ongs import Ong
from app.models.users import User
from app.models.addresses import Address
from app.schemas.ongs import OngIn


class OngRepository(ABC):

    @abstractmethod
    async def add(ong: OngIn, user: User, address: Address):
        async with AsyncSessionLocal() as session:
            ong = Ong(
                name=ong.name,
                business_name=ong.business_name,
                state_registration=ong.state_registration,
                phone_number=ong.phone_number,
                cnpj=ong.cnpj,
                address=address
            )

            ong.users.append(user)

            session.add(ong)
            await session.commit()
            await session.refresh(ong)

        return ong