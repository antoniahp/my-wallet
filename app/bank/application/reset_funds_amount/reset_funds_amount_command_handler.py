from bank.application.reset_funds_amount.reset_funds_amount_command import ResetFundsAmountCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.account_updater import AccountUpdater
from bank.domain.exceptions.account_movements.account_has_no_movements_exception import AccountHasNoMovementsException
from bank.domain.historic_movement_repository import HistoricMovementRepository
from cqrs.commands.command_handler import CommandHandler


class ResetFundsAmountCommandHandler(CommandHandler):
    def __init__(self, historic_movement_repository: HistoricMovementRepository, account_repository: AccountRepository, account_updater: AccountUpdater):
        self.__historic_movement_repository = historic_movement_repository
        self.__account_repository = account_repository
        self.__account_updater = account_updater

    def handle(self, command: ResetFundsAmountCommand):
        all_accounts = self.__account_repository.filter_accounts()
        for account in all_accounts:
           if all_accounts == 0:
               raise AccountHasNoMovementsException()
           last_account_movement = self.__historic_movement_repository.filter_movement(source_account=account.id)
           updated_account = self.__account_updater.update(
               account=account,
               funds_amount=last_account_movement[0].balance
           )
           self.__account_repository.save_account(updated_account)
