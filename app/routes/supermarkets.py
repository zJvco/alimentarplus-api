from fastapi import APIRouter, HTTPException, status

from app.repositories.supermarkets import SupermarketRepository
from app.schemas.supermarket import Supermarket

supermarket_router = APIRouter(
    prefix="/supermarkets"
)

@supermarket_router.get("/")
async def get_supermarkets():
    supermarkets = await SupermarketRepository.get_all()

    if not supermarkets:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum supermercado registrado"
        )
    return supermarkets

@supermarket_router.get("/{id}")
async def get_supermarket(id: int):
    supermarket = await SupermarketRepository.get_by_id(id)

    if not supermarket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum supermercado registrado"
        )
    return supermarket
