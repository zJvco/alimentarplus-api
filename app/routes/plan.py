from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.repositories.plan import PlanRepository
from app.schemas.plan import PlanIn, PlanOut
from app.utils import token_required

plan_router = APIRouter(
    prefix="/plans",
    dependencies=[Depends(token_required)]
)


@plan_router.get("/", response_model=List[PlanOut])
async def get_all_plans():
    plans = await PlanRepository.get_all()

    return plans