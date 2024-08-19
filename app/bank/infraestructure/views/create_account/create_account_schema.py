from datetime import date
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


class CreateAccountSchema(BaseModel):
    user_id: str
    identification_number: str
    account_number: str
    funds_amount: Decimal