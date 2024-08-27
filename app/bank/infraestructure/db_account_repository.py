from decimal import Decimal
from typing import Optional

from bank.domain.account import Account
from bank.domain.account_repository import AccountRepository


class DbAccountRepository(AccountRepository):

    def get_account_by_iban(self, account_number: str, select_for_update: bool = False) -> Optional[Account]:
        queryset =  Account.objects.filter(account_number=account_number).first()
        if select_for_update:
            return queryset.select_for_update()
        return queryset



    def save_account(self, account: Account) -> None:
        account.save()
