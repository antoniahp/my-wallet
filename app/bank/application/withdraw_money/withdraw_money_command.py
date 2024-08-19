from dataclasses import dataclass


@dataclass(frozen=True)
class WithdrawAmountCommand:
    user_id: str
    account_number: str
    withdraw_amount: int