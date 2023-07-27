from fastapi import APIRouter, HTTPException

from app.services.users import UserService
from app.schemas.users import UserCreateInput

user_router = APIRouter(prefix="/users")


# Obter todos os usuarios
@user_router.get("/")
async def get_users():
    result = await UserService().get_all_users()

    return result


# Criar um usuario
@user_router.post("/")
async def create_user(user_data: UserCreateInput):
    await UserService().create_user(user_data)

    return


# Deletar um usuario
@user_router.delete("/{user_id}")
async def delete_user():
    pass


# Obter um usuario
@user_router.get("/{user_id}")
async def get_user():
    pass