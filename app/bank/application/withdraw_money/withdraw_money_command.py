from dataclasses import dataclass
from unicodedata import decimal
from uuid import UUID


@dataclass(frozen=True)
class WithdrawAmountCommand:
    historic_movement_id: UUID
    user_id: UUID
    source_account: UUID
    withdraw_amount: decimal
    concept: str
