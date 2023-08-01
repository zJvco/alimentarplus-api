from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.users import UserCreateInput
from app.repositories.users import UserRepository

user_router = APIRouter(prefix="/users")


# Obter todos os usuarios
@user_router.get("/")
async def get_users():
    users = await UserRepository.get_all()

    return users


# Criar um usuario (sem ser o principal)
@user_router.post("/")
async def create_user(user_data: UserCreateInput):
    user = await UserRepository.add(
            user_data.name,
            user_data.email,
            user_data.phone_number,
            user_data.cpf,
            user_data.password
        )
    
    return user


# Deletar um usuario
@user_router.delete("/{user_id}")
async def delete_user():
    pass


# Obter um usuario
@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    user = await UserRepository.get_by_id(user_id)
    
    return user