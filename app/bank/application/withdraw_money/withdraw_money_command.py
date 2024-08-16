from dataclasses import dataclass


@dataclass(frozen=True)
class WithdrawAmountCommand:
    account_number: str
    withdraw_amount: int