from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TransferMoneySchema(BaseModel):
    source_account: UUID
    target_account: UUID
    amount_to_send: Decimal
    concept: Optional[str]