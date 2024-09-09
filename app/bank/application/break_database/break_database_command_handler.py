from decimal import Decimal

from bank.application.break_database.break_database_command import BreakDatabaseCommand
from bank.domain.account_repository import AccountRepository
from cqrs.commands.command_handler import CommandHandler


class BreakDatabaseCommandHandler(CommandHandler):
    def __init__(self, account_repository: AccountRepository):
        self.__account_repository = account_repository


    def handle(self, command:BreakDatabaseCommand):
        all_accounts = self.__account_repository.filter_accounts()
        accounts_modified = []
        new_funds_amount =Decimal(0.0)
        for account in all_accounts:
            account.funds_amount = new_funds_amount
            accounts_modified.append(account)

        for account in accounts_modified:
            self.__account_repository.save_account(account)