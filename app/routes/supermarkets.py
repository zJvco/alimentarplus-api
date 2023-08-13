from fastapi import APIRouter, HTTPException

from app.repositories.supermarkets import SupermarketRepository

supermarket_router = APIRouter(
    prefix="/supermarkets"
)

@supermarket_router.get("/")
async def get_supermarkets():
    supermarkets = await SupermarketRepository.get_all()

    if not supermarkets:
        raise HTTPException(
            status_code=404,
            detail="Nenhum supermercado registrado"
        )

    return supermarkets