from datetime import date
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class CreateAccountSchema(BaseModel):
    account_number: str
    funds_amount: Decimal