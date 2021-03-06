# project/app/api/crud.py


from typing import List, Optional

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(url=payload.url, summary="dummy summary")

    await summary.save()
    return summary.id


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def get(id: int) -> Optional[dict]:
    summary = await TextSummary.get_or_none(id=id)
    return summary
