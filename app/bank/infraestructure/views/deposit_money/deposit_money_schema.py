from decimal import Decimal

from pydantic import BaseModel

class DepositMoneySchema(BaseModel):
    account_number: str
    deposit_amount: Decimal
    concept: str