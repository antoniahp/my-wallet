import uuid
from decimal import Decimal
from bank.domain.account import Account



class AccountCreator:
    def create(self, account_number: str, funds_amount:Decimal, user_id: uuid):
        return Account(
            account_number=account_number,
            funds_amount=funds_amount,
            user_id=user_id,
        )