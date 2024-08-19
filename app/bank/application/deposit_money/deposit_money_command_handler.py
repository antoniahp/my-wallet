from bank.application.deposit_money.deposit_money_command import DepositAmountCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.exceptions.deposit_money.account_not_found_exception import AccountNotFoundException


class DepositMoneyCommandHandler:
    def __init__(self, account_repository:AccountRepository):
        self.account_repository = account_repository


    def handle(self, command:DepositAmountCommand):
        account_filtered = self.account_repository.get_account_by_iban(account_number=command.account_number)
        if account_filtered is None:
            raise AccountNotFoundException(account_number=command.account_number)
        account_filtered.funds_amount = account_filtered.funds_amount + command.deposit_amount
        self.account_repository.save_account(account_filtered)
