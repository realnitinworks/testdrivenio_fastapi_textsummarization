# project/app/api/crud.py


from typing import Optional, List
from app.models.tortoise import TextSummary
from app.models.pydantic import SummaryPayloadSchema


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary"
    )

    await summary.save()
    return summary.id


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.get_or_none(id=id)
    return summary