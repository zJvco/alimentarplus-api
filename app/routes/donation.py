from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.schemas.donation import DonationIn, DonationOut
from app.repositories.donation import DonationRepository
from app.utils import token_required
from app.repositories.supermarket import SupermarketRepository
from app.repositories.ong import OngRepository
from app.repositories.product import ProductRepository
from app.schemas.product import ProductIn

donation_router = APIRouter(
    prefix="/donations",
    dependencies=[Depends(token_required)]
)


@donation_router.get("/", response_model=List[DonationOut])
async def get_donations():
    donations = await DonationRepository.get_all()

    if not donations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma doação disponivel no momento"
        )

    return donations


@donation_router.post("/", response_model=DonationOut)
async def create_donation(data: DonationIn):
    product = await ProductRepository.get_by_id(data.id_product)
    product.is_active = False

    try:
        await ProductRepository.update(product.id, dict(ProductIn(**product.__dict__)))
    except:
        HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Não foi possível atualizar o campo 'is_active' do produto"
        )

    donation = await DonationRepository.add(data)

    return donation