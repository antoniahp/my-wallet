from dataclasses import dataclass
from decimal import Decimal
from typing import Optional
from uuid import UUID


@dataclass(frozen=True)
class DepositAmountCommand:
    historic_movement_id: UUID
    user_id: UUID
    deposit_amount: Decimal
    concept: str
    source_account: UUID
