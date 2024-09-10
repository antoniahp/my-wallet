from django.core.management import BaseCommand

from bank.application.reset_funds_amount.reset_funds_amount_command import ResetFundsAmountCommand
from bank.application.reset_funds_amount.reset_funds_amount_command_handler import ResetFundsAmountCommandHandler
from bank.domain.account_repository import AccountRepository
from bank.domain.account_updater import AccountUpdater
from bank.domain.historic_movement_repository import HistoricMovementRepository
from bank.infraestructure.db_account_repository import DbAccountRepository
from bank.infraestructure.db_historic_movemen_repository import DbHistoricMovementRepository


class Command(BaseCommand):
    help = 'Reset found amount of account'

    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__account_updater = AccountUpdater()
        self.__db_historic_movement_repository = DbHistoricMovementRepository()
        self.__reset_funds_amount_command_handler = ResetFundsAmountCommandHandler(account_repository=self.__db_account_repository, account_updater=self.__account_updater, historic_movement_repository=self.__db_historic_movement_repository)

    def handle(self, *args, **options):
        command = ResetFundsAmountCommand()
        self.__reset_funds_amount_command_handler.handle(command)
