from datetime import datetime, timedelta

from django.core.management import BaseCommand

from bank.application.commission_calculated.commission_calculated_command import CommissionCalculatedCommand
from bank.application.commission_calculated.commission_calculated_command_handler import CommissionCalculatedCommandHandler
from bank.domain.commissions_calculated_creator import CommissionsCalculatedCreator
from bank.domain.historic_movement_repository import HistoricMovementRepository
from bank.infraestructure.db_commissions_calculated_repository import DbCommissionsCalculatedRepository
from bank.infraestructure.db_historic_movemen_repository import DbHistoricMovementRepository


class Command(BaseCommand):
    help = 'Calculates the commissions'

    def __init__(self):
        super().__init__()
        self.__db_commissions_calculated_repository = DbCommissionsCalculatedRepository()
        self.__commissions_calculated_creator = CommissionsCalculatedCreator()
        self.__db_historic_movement_repository = DbHistoricMovementRepository()
        self.__commission_calculated_command_handler = CommissionCalculatedCommandHandler(
            commissions_calculated_repository=self.__db_commissions_calculated_repository,
            commissions_calculated_creator=self.__commissions_calculated_creator,
            historic_movement_repository= self.__db_historic_movement_repository,
        )
    def handle(self, *args, **options):
        command = CommissionCalculatedCommand(date=(datetime.now()).date(), hours_commission_calculated=24) #date=(datetime.now() - timedelta(days=1)).date()
        self.__commission_calculated_command_handler.handle(command)
