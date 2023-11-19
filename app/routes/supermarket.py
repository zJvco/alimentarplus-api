from fastapi import APIRouter, HTTPException, status
from typing import List

from app.repositories.supermarket import SupermarketRepository
from app.schemas.supermarket import SupermarketIn, SupermarketOut
from app.repositories.product import ProductRepository
from app.schemas.product import ProductIn, ProductOut

supermarket_router = APIRouter(
    prefix="/supermarkets"
)

@supermarket_router.get("/", response_model=List[SupermarketOut])
async def get_supermarkets():
    supermarkets = await SupermarketRepository.get_all()

    if not supermarkets:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum supermercado registrado"
        )
    
    return supermarkets

@supermarket_router.get("/{id}", response_model=SupermarketOut)
async def get_supermarket_by_id(id: int):
    supermarket = await SupermarketRepository.get_by_id(id)

    if not supermarket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhum supermercado registrado"
        )
    
    return supermarket

@supermarket_router.get("/{supermarket_id}/products", response_model=List[ProductOut])
async def get_supermarket_products(supermarket_id: int):
    products = await ProductRepository.get_all_products_by_supermarket_id(supermarket_id)

    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O supermercado não possui nenhum produto"
        )

    return products

@supermarket_router.post("/{supermarket_id}/products", response_model=ProductOut)
async def create_product(supermarket_id: int, product_data: ProductIn):
    try:
        product = await ProductRepository.add_product_by_supermarket_id(supermarket_id, product_data)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao criar o produto"
        )
    
    return product