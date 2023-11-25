from fastapi import APIRouter, HTTPException, status
from typing import List

from app.repositories.ong import OngRepository
from app.schemas.ong import OngIn, OngOut

ong_router = APIRouter(
    prefix="/ongs"
)
# 
@ong_router.get("/", response_model=List[OngOut])
async def get_ongs():
    ongs = await OngRepository.get_all()

    if not ongs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma ong registrado"
        )
    return ongs


@ong_router.get("/{id}")
async def get_ong_by_id(id: int):
    ong = await OngRepository.get_by_id(id)

    if not ong:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma ong registrado"
        )
    return ong


@ong_router.post("/")
async def create(ong: OngIn):
    new_ong = await OngRepository.add(ong)
    return new_ong


@ong_router.put("/")
async def update(ong: OngIn):
    data = OngRepository.update(ong)
    return data


@ong_router.put("/update-address")
async def update_address(ong: OngIn):
    data = OngRepository.update_address(ong)
    return data


@ong_router.delete("/{id}")
async def delete_ong(id: int):
    ...
    