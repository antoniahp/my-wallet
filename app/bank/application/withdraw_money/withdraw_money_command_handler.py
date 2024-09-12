from decimal import Decimal

from django.db import transaction

from bank.application.withdraw_money.withdraw_money_command import WithdrawAmountCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.commisions_by_country_choices import CommissionsByCountryChoices
from bank.domain.commissions_by_country_repository import CommissionsByCountryRepository
from bank.domain.exceptions.account_movements.cannot_operate_on_this_account_exception import CanNotOperateOnThisAccountException
from bank.domain.exceptions.withdraw_money.account_not_found_exception import AccountNotFoundException
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.domain.historic_movement_repository import HistoricMovementRepository
from bank.domain.movement_categories import MovementCategories


class WithdrawMoneyCommandHandler:
    def __init__(self, account_repository:AccountRepository, historic_movement_repository: HistoricMovementRepository, historic_movement_creator: HistoricMovementCreator, commissions_by_country_repository: CommissionsByCountryRepository):
        self.account_repository = account_repository
        self.historic_movement_repository = historic_movement_repository
        self.historic_movement_creator = historic_movement_creator
        self.commissions_by_country_repository = commissions_by_country_repository


    def handle(self, command:WithdrawAmountCommand):
        with transaction.atomic():
            account_filtered = self.account_repository.get_account_by_id(source_account=command.source_account, select_for_update=True)
            if "ES" in account_filtered.account_number:
                country = CommissionsByCountryChoices.SPAIN.value
            elif "PT" in account_filtered.account_number:
                country = CommissionsByCountryChoices.PORTUGAL.value
            else:
                country = CommissionsByCountryChoices.FRANCE.value


            commission_applied = self.commissions_by_country_repository.filter_commissions(country=country, range_max_gte=command.withdraw_amount, range_min_lte=command.withdraw_amount)


            if account_filtered.user_id != command.user_id:
                raise CanNotOperateOnThisAccountException()

            if account_filtered is None:
                raise AccountNotFoundException(account_number=command.source_account)

            if commission_applied is None:
                commission_percentage = Decimal(0)
            else:
                commission_percentage = commission_applied.commission_percentage

            total = command.withdraw_amount + commission_percentage

            if account_filtered.funds_amount >= total:
                account_filtered.funds_amount = account_filtered.funds_amount - total
                historic_movement = self.historic_movement_creator.create(
                    source_account_id=account_filtered.id,
                    category=MovementCategories.WITHDRAW_MONEY.value,
                    balance=account_filtered.funds_amount,
                    delta_amount=command.withdraw_amount + commission_percentage ,
                    concept=command.concept,
                    target_account_id=None,
                    commission=commission_percentage,
                    country=country
                )
                self.historic_movement_repository.save_movement(historic_movement)
                self.account_repository.save_account(account_filtered)
