from decimal import Decimal

from bank.application.reset_funds_amount.reset_funds_amount_command import ResetFundsAmountCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.exceptions.account_movements.account_has_no_movements_exception import AccountHasNoMovementsException
from bank.domain.historic_movement_repository import HistoricMovementRepository
from cqrs.commands.command_handler import CommandHandler


class ResetFundsAmountCommandHandler(CommandHandler):
    def __init__(self, historic_movement_repository: HistoricMovementRepository, account_repository: AccountRepository):
        self.__historic_movement_repository = historic_movement_repository
        self.__account_repository = account_repository

    def handle(self, command: ResetFundsAmountCommand):
        all_accounts = self.__account_repository.filter_accounts()
        for account in all_accounts:
           last_account_movement = self.__historic_movement_repository.filter_movements(source_account=account.id)
           funds_amount = Decimal(0.0)
           if last_account_movement:
                funds_amount = last_account_movement[0].balance
           account.funds_amount = funds_amount


           self.__account_repository.save_account(account)
