from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class DepositMoneySchema(BaseModel):
    source_account: UUID
    deposit_amount: Decimal
    concept: Optional[str]
