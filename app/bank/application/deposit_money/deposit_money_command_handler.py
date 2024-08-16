from bank.application.deposit_money.deposit_money_command import DepositAmountCommand
from bank.domain.account_repository import AccountRepository


class DepositMoneyCommandHandler:
    def __init__(self, account_repository:AccountRepository):
        self.account_repository = account_repository


    def handle(self, command:DepositAmountCommand):
        account_filtered = self.account_repository.get_account_by_iban(account_number=command.account_number)
        account_filtered.funds_amount = account_filtered.funds_amount + command.withdraw_amount
        self.account_repository.save_account(account_filtered)
