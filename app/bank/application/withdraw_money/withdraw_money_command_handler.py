from bank.application.withdraw_money.withdraw_money_command import WithdrawAmountCommand
from bank.domain.account_repository import AccountRepository


class WithdrawMoneyCommandHandler:
    def __init__(self, account_repository:AccountRepository):
        self.account_repository = account_repository


    def handle(self, command:WithdrawAmountCommand):

        account_filtered = self.account_repository.get_account_by_iban(account_number=command.account_number)
        if account_filtered.funds_amount >= command.withdraw_amount:
            account_filtered.funds_amount = account_filtered.funds_amount - command.withdraw_amount
            self.account_repository.save_account(account_filtered)
