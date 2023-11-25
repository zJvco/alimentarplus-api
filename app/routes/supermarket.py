from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.repositories.supermarket import SupermarketRepository
from app.schemas.supermarket import SupermarketIn, SupermarketOut
from app.repositories.product import ProductRepository
from app.schemas.product import ProductIn, ProductOut
from app.utils import token_required

supermarket_router = APIRouter(
    prefix="/supermarkets",
    dependencies=[Depends(token_required)]
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

@supermarket_router.get("/{supermarket_id}/products/{product_id}", response_model=ProductOut)
async def get_supermarket_product(supermarket_id: int, product_id: int):
    product = await ProductRepository.get_product_by_supermarket_id(supermarket_id, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O produto não existe neste supermercado"
        )

    return product

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

@supermarket_router.put("/{supermarket_id}/products/{product_id}")
async def update_product(supermarket_id: int, product_id: int, product_data: ProductIn):
    result = await ProductRepository.update(product_id, dict(product_data))

    return { "id": result }

@supermarket_router.delete("/{supermarket_id}/products/{product_id}")
async def delete_product(supermarket_id: int, product_id: int):
    result = await ProductRepository.delete(product_id)

    return { "id": result }