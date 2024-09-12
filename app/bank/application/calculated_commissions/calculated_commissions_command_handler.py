from bank.application.calculated_commissions.calculated_commissions_command import CalculatedCommissionsCommand
from bank.domain.calculated_commissions_creator import CalculatedCommissionsCreator
from bank.domain.calculated_commissions_repository import CalculatedCommissionsRepository
from bank.domain.historic_movement_repository import HistoricMovementRepository


class CalculatedCommissionsCommandHandler:
    def __init__(self, calculated_commissions_repository: CalculatedCommissionsRepository, historic_movement_repository: HistoricMovementRepository, calculated_commissions_creator: CalculatedCommissionsCreator ):
        self.__calculated_commissions_repository = calculated_commissions_repository
        self.__historic_movement_repository = historic_movement_repository
        self.__calculated_commissions_creator = calculated_commissions_creator

    def handle(self, command:CalculatedCommissionsCommand):
        # calcular las comisiones del dia filtrando por dia y pais
        # variable donde guaradmos todas las comisiones que cumplan x condiciones
        commissions_filtered = self.__historic_movement_repository.filter_movements(country=command.country, date=command.date)
        self.__calculated_commissions_creator.create(
            country=commissions_filtered.country,
            date=commissions_filtered.created_at,
            total_amount_commission=commissions_filtered.commission
        )



        # por historico en historico dame los que seam de españa
    # crear entrda de comisiones
    #guardarla

    pass