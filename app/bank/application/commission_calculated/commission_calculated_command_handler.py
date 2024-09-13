from bank.application.commission_calculated.commission_calculated_command import CommissionCalculatedCommand
from bank.domain.commissions_calculated_creator import CommissionsCalculatedCreator
from bank.domain.commissions_calculated_repository import CommissionsCalculatedRepository
from bank.domain.historic_movement_repository import HistoricMovementRepository
from cqrs.commands.command_handler import CommandHandler


class CommissionCalculatedCommandHandler(CommandHandler):
    def __init__(self, commissions_calculated_creator: CommissionsCalculatedCreator,
                 commissions_calculated_repository: CommissionsCalculatedRepository,
                 historic_movement_repository: HistoricMovementRepository):

        self.__commissions_calculated_creator = commissions_calculated_creator
        self.__commissions_calculated_repository = commissions_calculated_repository
        self.__historic_movement_repository = historic_movement_repository

    def handle(self, command: CommissionCalculatedCommand):
        commissions_filtered_by_date = self.__historic_movement_repository.filter_movements(created_at=command.date)
        countries = {}

        for movement in commissions_filtered_by_date:
            country = movement.country
            commission = movement.commission
            if country in countries:
                countries[country] = countries[country] + commission
            else:
                countries[country] = commission

        for country, total_amount_commission in countries.items():
            commission = self.__commissions_calculated_creator.create(
                country=country,
                total_amount_commission=total_amount_commission,
                date=command.date
            )

            self.__commissions_calculated_repository.save_commissions_calculated(commission)

