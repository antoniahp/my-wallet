from django.core.management import BaseCommand

from bank.application.break_database.break_database_command import BreakDatabaseCommand
from bank.application.break_database.break_database_command_handler import BreakDatabaseCommandHandler
from bank.infraestructure.db_account_repository import DbAccountRepository


class Command(BaseCommand):
    help = 'We put the funds in the accounts to 0'

    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__break_database_command_handler = BreakDatabaseCommandHandler(self.__db_account_repository )

    def handle(self, *args, **options):
        command = BreakDatabaseCommand()
        self.__break_database_command_handler.handle(command)
