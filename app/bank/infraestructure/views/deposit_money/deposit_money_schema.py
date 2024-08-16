from pydantic import BaseModel

class DepositMoneySchema(BaseModel):
    account_number: str
    withdraw_amount: int