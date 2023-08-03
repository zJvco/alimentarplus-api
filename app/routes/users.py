from fastapi import APIRouter, HTTPException, Depends

from app.schemas.users import UserIn
from app.repositories.users import UserRepository
from app.utils import token_required

user_router = APIRouter(prefix="/users")


# Obter todos os usuarios
@user_router.get("/")
async def get_users(current_user: str = Depends(token_required)):
    users = await UserRepository.get_all()


    return users 


# Criar um usuario (sem ser o principal)
@user_router.post("/")
async def create_user(user_data: UserIn, current_user: str = Depends(token_required)):
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
async def delete_user(current_user: str = Depends(token_required)):
    pass


# Obter um usuario
@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int, current_user: str = Depends(token_required)):
    user = await UserRepository.get_by_id(user_id)

    return user