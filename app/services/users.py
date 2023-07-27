from typing import List

from app.repositories.users import UserRepository
from app.schemas.users import UserCreateInput


class UserService:
    async def get_all_users(self) -> List:
        users = await UserRepository.get_all()

        return users
    
    async def create_user(self, user_data: UserCreateInput) -> None:
        user = await UserRepository.create(
            user_data.name,
            user_data.email,
            user_data.phone_number,
            user_data.cpf,
            user_data.password
        )

        return user
