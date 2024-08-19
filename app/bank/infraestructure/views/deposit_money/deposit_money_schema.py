from pydantic import BaseModel

class DepositMoneySchema(BaseModel):
    user_id: str
    account_number: str
    deposit_amount: int