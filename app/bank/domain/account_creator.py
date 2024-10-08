from decimal import Decimal
from uuid import UUID
from bank.domain.account import Account
from bank.domain.account_repository import AccountRepository
from bank.domain.exceptions.create_account.account_already_exists_exception import AccountAlreadyExistsException


class AccountCreator:

    def __init__(self, account_repository:AccountRepository,):
        self.account_repository = account_repository

    def create(self, account_id:UUID, account_number: str, funds_amount:Decimal, user_id: str):
        validate_account_number = self.account_repository.get_account_by_id(source_account=account_id)
        if validate_account_number is not None:
            raise AccountAlreadyExistsException(account_number=account_number)

        return Account(
            account_id = account_id,
            account_number=account_number,
            funds_amount=funds_amount,
            user_id=user_id,
        )
