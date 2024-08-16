from dataclasses import dataclass

@dataclass(frozen=True)
class DepositAmountCommand:
    account_number: str
    withdraw_amount: int