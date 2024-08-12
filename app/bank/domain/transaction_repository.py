from abc import ABC, abstractmethod

from bank.domain.account import Account


class TransactionRepository(ABC):
    @abstractmethod
    def get_account_by_iban(self, iban: str) -> Account:
        pass

    @abstractmethod
    def update_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def save_account(self, account: Account) -> None:
        pass

