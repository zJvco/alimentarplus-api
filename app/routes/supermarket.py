from fastapi import APIRouter, HTTPException, status, Depends, Request
from typing import List
from datetime import datetime, timedelta

from app.repositories.supermarket import SupermarketRepository
from app.schemas.supermarket import SupermarketIn, SupermarketOut
from app.repositories.product import ProductRepository
from app.repositories.donation import DonationRepository
from app.schemas.product import ProductIn, ProductOut
from app.schemas.donation import DonationOut
from app.schemas.plan import UpdatePlanIn
from app.repositories.plan import PlanRepository
from app.utils import token_required

supermarket_router = APIRouter(
    prefix="/supermarkets",
    dependencies=[Depends(token_required)]
)

#
# Rotas de supermercado para criar, deletar, atualizar, obter e obter vários
#

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

#
# Rotas de produtos para criar, deletar, atualizar, obter e obter vários
#

@supermarket_router.get("/{supermarket_id}/products", response_model=List[ProductOut])
async def get_all_supermarket_products(supermarket_id: int):
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
    id = await ProductRepository.update(product_id, dict(product_data))

    return { "id": id }


@supermarket_router.delete("/{supermarket_id}/products/{product_id}")
async def delete_product(supermarket_id: int, product_id: int):
    id = await ProductRepository.delete(product_id)

    return { "id": id }

#
# Rotas de doação para criar, deletar, atualizar, obter e obter várias
#

@supermarket_router.get("/{supermarket_id}/donations", response_model=List[DonationOut])
async def get_all_supermarket_donations(supermarket_id: int):
    donations = await DonationRepository.get_all_donations_by_supermarket_id(supermarket_id)

    if not donations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma doação disponivel no momento"
        )
    
    return donations

#
# Rotas para atualizar o plano do supermercado
#
    
@supermarket_router.post("/{supermarket_id}/update-plan")
async def update_supermarket_plan(supermarket_id: int, plan_id: UpdatePlanIn):
    id = await SupermarketRepository.update_plan(supermarket_id, plan_id.id)

    return { "id": id }

#
# Rotas de dados dos dashboards
#

@supermarket_router.get("/{supermarket_id}/dashboard/donations-last-30-days", response_model=List[DonationOut])
async def get_supermarket_donations_last_30_days(supermarket_id: int):
    todays_date = datetime.now()
    start_date = todays_date - timedelta(days=30)

    donations = await DonationRepository.get_last_30_days_donations_by_supermarket_id(supermarket_id, start_date.strftime('%Y-%m-%d'))

    return donations