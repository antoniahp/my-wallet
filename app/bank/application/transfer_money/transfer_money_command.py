from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class TransferMoneyCommand:
    user_id: str
    sender_account_number: str
    recipient_account_number: str
    amount_to_send: Decimal