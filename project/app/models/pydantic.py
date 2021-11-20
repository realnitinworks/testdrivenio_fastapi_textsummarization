# project/app/models/pydantic.py


from pydantic import BaseModel
from datetime import datetime


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
