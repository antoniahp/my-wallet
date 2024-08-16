from pydantic import BaseModel

class DepositMoneySchema(BaseModel):
    account_number: str
    deposit_amount: int