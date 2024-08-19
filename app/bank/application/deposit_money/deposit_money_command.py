from dataclasses import dataclass

@dataclass(frozen=True)
class DepositAmountCommand:
    user_id: str
    account_number: str
    deposit_amount: int