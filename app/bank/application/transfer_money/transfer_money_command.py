from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class TransferMoneyCommand:
    historic_movement_id: UUID
    user_id: UUID
    sender_account_id: UUID
    recipient_account_id: UUID
    amount_to_send: Decimal
    concept: str