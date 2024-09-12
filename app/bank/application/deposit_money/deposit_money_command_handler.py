from decimal import Decimal

from django.db import transaction
from bank.application.deposit_money.deposit_money_command import DepositAmountCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.commisions_by_country_choices import CommissionsByCountryChoices
from bank.domain.exceptions.account_movements.cannot_operate_on_this_account_exception import CanNotOperateOnThisAccountException
from bank.domain.exceptions.deposit_money.account_not_found_exception import AccountNotFoundException
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.domain.historic_movement_repository import HistoricMovementRepository
from bank.domain.movement_categories import MovementCategories


class DepositMoneyCommandHandler:
    def __init__(self, account_repository: AccountRepository, historic_movement_repository: HistoricMovementRepository, historic_movement_creator: HistoricMovementCreator):
        self.account_repository = account_repository
        self.historic_movement_repository = historic_movement_repository
        self.historic_movement_creator = historic_movement_creator

    def handle(self, command:DepositAmountCommand):
        with transaction.atomic():
            account_filtered = self.account_repository.get_account_by_id(source_account=command.source_account,select_for_update=True)

            if "ES" in account_filtered.account_number:
                country = CommissionsByCountryChoices.SPAIN.value
            elif "PT" in account_filtered.account_number:
                country = CommissionsByCountryChoices.PORTUGAL.value
            else:
                country = CommissionsByCountryChoices.FRANCE.value

            if account_filtered.user_id != command.user_id:
                raise CanNotOperateOnThisAccountException()

            if account_filtered is None:
                raise AccountNotFoundException(source_account=command.source_account)

            account_filtered.funds_amount = account_filtered.funds_amount + command.deposit_amount
            historic_movement = self.historic_movement_creator.create(
                source_account_id=account_filtered.id,
                category=MovementCategories.DEPOSIT_MONEY.value,
                balance=account_filtered.funds_amount,
                delta_amount=command.deposit_amount,
                concept=command.concept,
                target_account_id=None,
                commission=Decimal(0),
                country = country
            )

            self.historic_movement_repository.save_movement(historic_movement)
            self.account_repository.save_account(account_filtered)
