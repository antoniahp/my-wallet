from decimal import Decimal
from pydantic import BaseModel

class CreateAccountSchema(BaseModel):
    account_number: str
    funds_amount: Decimal
