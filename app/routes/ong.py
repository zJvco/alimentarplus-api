from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.repositories.ong import OngRepository
from app.schemas.ong import OngOut
from app.schemas.donation import DonationOut
from app.repositories.donation import DonationRepository
from app.utils import token_required

ong_router = APIRouter(
    prefix="/ongs",
    dependencies=[Depends(token_required)]
)


@ong_router.get("/", response_model=List[OngOut])
async def get_ongs():
    ongs = await OngRepository.get_all()

    return ongs


@ong_router.get("/{ong_id}", response_model=OngOut)
async def get_ong_by_id(ong_id: int):
    ong = await OngRepository.get_by_id(ong_id)

    return ong


@ong_router.get("/{ong_id}/donations", response_model=List[DonationOut])
async def get_all_ong_donations(ong_id: int):
    donations = await DonationRepository.get_all_donations_by_ong_id(ong_id)

    return donations
    