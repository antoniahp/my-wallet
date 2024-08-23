from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class TransferMoneyCommand:
    user_id: UUID
    sender_account_number: str
    recipient_account_number: str
    amount_to_send: Decimal