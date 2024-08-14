from uuid import UUID
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CreateAccountCommand:
    identification_number: str
    account_id: UUID
    account_number: str
    funds_amount: Decimal
