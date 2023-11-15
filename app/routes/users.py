from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.schemas.users import UserIn, UserOut
from app.repositories.users import UserRepository
from app.utils import token_required

user_router = APIRouter(
    prefix="/users",
    dependencies=[Depends(token_required)]
)


# Obter todos os usuarios
@user_router.get("/", response_model=List[UserOut])
async def get_users():
    users = await UserRepository.get_all()

    if not users:
        raise HTTPException(
            status_code=404,
            detail="Nenhum usuário cadastrado ainda"
        )
    
    return users


# Criar um usuario (sem ser o principal)
@user_router.post("/", response_model=UserOut)
async def create_user(user_data: UserIn):
    try:
        user = await UserRepository.add(
                user_data.name,
                user_data.email,
                user_data.phone_number,
                user_data.cpf,
                user_data.password
            )
    except:
        raise HTTPException(
            status_code=400,
            detail="Usuário não pode ser criado"
        )
    
    return user


# Deletar um usuario
@user_router.delete("/{user_id}")
async def delete_user(user_id: int):
    try:
        await UserRepository.delete(user_id)
    except:
        raise HTTPException(
            status_code=400,
            detail="Não foi possível excluir o usuário"
        )
    
    return user_id


# Obter um usuario
@user_router.get("/{user_id}", response_model=UserOut)
async def get_user_by_id(user_id: int):
    user = await UserRepository.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )
    
    return user