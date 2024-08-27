from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class DepositAmountCommand:
    user_id: UUID
    account_number: str
    deposit_amount: Decimal
    concept: str
