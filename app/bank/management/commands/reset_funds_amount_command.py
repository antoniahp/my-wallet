from django.core.management import BaseCommand

from bank.application.reset_funds_amount.reset_funds_amount_command import ResetFundsAmountCommand
from bank.application.reset_funds_amount.reset_funds_amount_command_handler import ResetFundsAmountCommandHandler
from bank.infraestructure.db_account_repository import DbAccountRepository
from bank.infraestructure.db_historic_movemen_repository import DbHistoricMovementRepository


class Command(BaseCommand):
    help = 'Reset found amount of account'

    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__db_historic_movement_repository = DbHistoricMovementRepository()
        self.__reset_funds_amount_command_handler = ResetFundsAmountCommandHandler(account_repository=self.__db_account_repository, historic_movement_repository=self.__db_historic_movement_repository)

    def handle(self, *args, **options):
        command = ResetFundsAmountCommand()
        self.__reset_funds_amount_command_handler.handle(command)
