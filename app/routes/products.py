from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.repositories.product import ProductRepository
from app.schemas.product import ProductOut
from app.utils import token_required

products_router = APIRouter(
    prefix="/products",
    dependencies=[Depends(token_required)]
)


@products_router.get("/", response_model=List[ProductOut])
async def get_all_products():
    products = await ProductRepository.get_all()

    return products


@products_router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: int):
    product = await ProductRepository.get_by_id(product_id)

    return product