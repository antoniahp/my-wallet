from pydantic import BaseModel


class WithdrawMoneySchema(BaseModel):
    account_number: str
    withdraw_amount: int