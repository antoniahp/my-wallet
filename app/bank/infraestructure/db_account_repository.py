from decimal import Decimal
from typing import Optional
from uuid import UUID

from bank.domain.account import Account
from bank.domain.account_repository import AccountRepository


class DbAccountRepository(AccountRepository):

    def get_account_by_id(self, source_account: UUID, select_for_update: bool = False) -> Optional[Account]:
        queryset = Account.objects.filter(id=source_account)
        if select_for_update:
            queryset = queryset.select_for_update()
        return queryset.first()



    def save_account(self, account: Account) -> None:
        account.save()
