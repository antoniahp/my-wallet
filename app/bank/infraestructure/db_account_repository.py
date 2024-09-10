from typing import Optional, List
from unicodedata import decimal
from uuid import UUID
from django.db.models import Q
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

    def filter_accounts(self, user_id:Optional[UUID]=None, account_number: Optional[str] = None, funds_amount: Optional[decimal] = None) -> List[Account]:
        filters = Q()
        if user_id is not None:
            filters = filters & Q(user_id=user_id)
        if account_number is not None:
            filters = filters & Q(account_number=account_number)
        if funds_amount is not None:
            filters = filters & Q(funds_amount=funds_amount)

        accounts = Account.objects.filter(filters)
        return accounts
