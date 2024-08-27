from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class WithdrawAmountCommand:
    user_id: UUID
    account_number: str
    withdraw_amount: int