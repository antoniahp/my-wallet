from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class WithdrawMoneySchema(BaseModel):
    source_account: UUID
    withdraw_amount: Decimal
    concept: Optional[str]