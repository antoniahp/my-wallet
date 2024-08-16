from decimal import Decimal
from typing import Optional

from bank.domain.account import Account
from bank.domain.account_repository import AccountRepository


class DbAccountRepository(AccountRepository):

    def get_account_by_iban(self, account_number: str) -> Optional[Account]:
        return Account.objects.filter(account_number=account_number).first()


    def save_account(self, account: Account) -> None:
        account.save()
