# project/app/api/summaries.py


from fastapi import APIRouter

from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.api import crud


router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    return {
        "id": summary_id,
        "url": payload.url
    }