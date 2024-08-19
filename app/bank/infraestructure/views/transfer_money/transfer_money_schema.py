from decimal import Decimal

from pydantic import BaseModel


class TransferMoneySchema(BaseModel):
    user_id: str
    sender_account_number: str
    recipient_account_number: str
    amount_to_send: Decimal