from app.repositories.user_repository import UserRepository


class UserService:
    async def get_all_users(self):
        users = await UserRepository.get_all()

        return users