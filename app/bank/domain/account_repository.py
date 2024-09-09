from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from bank.domain.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def get_account_by_id(self, source_account: UUID, select_for_update: bool = False) -> Optional[Account]:
        pass

    @abstractmethod
    def save_account(self, account: Account) -> None:
        pass


