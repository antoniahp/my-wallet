from pydantic import BaseModel


class WithdrawMoneySchema(BaseModel):
    user_id: str
    account_number: str
    withdraw_amount: int