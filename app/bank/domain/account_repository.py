from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List
from unicodedata import decimal
from uuid import UUID

from bank.domain.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def get_account_by_id(self, source_account: UUID, select_for_update: bool = False) -> Optional[Account]:
        pass

    @abstractmethod
    def save_account(self, account: Account) -> None:
        pass


    @abstractmethod
    def filter_accounts(self, account_number: Optional[str] = None, funds_amount: Optional[decimal] = None) -> List[Account]:
        pass
