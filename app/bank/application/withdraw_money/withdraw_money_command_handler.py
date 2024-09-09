from django.db import transaction

from bank.application.withdraw_money.withdraw_money_command import WithdrawAmountCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.exceptions.withdraw_money.account_not_found_exception import AccountNotFoundException
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.domain.historic_movement_repository import HistoricMovementRepository
from bank.domain.movement_categories import MovementCategories


class WithdrawMoneyCommandHandler:
    def __init__(self, account_repository:AccountRepository, historic_movement_repository: HistoricMovementRepository, historic_movement_creator: HistoricMovementCreator):
        self.account_repository = account_repository
        self.historic_movement_repository = historic_movement_repository
        self.historic_movement_creator = historic_movement_creator

    def handle(self, command:WithdrawAmountCommand):
        with transaction.atomic():
            account_filtered = self.account_repository.get_account_by_id(source_account=command.source_account, select_for_update=True)
            if account_filtered is None:
                raise AccountNotFoundException(source_account=command.source_account)

            if account_filtered.funds_amount >= command.withdraw_amount:
                account_filtered.funds_amount = account_filtered.funds_amount - command.withdraw_amount
                historic_movement = self.historic_movement_creator.create(
                    source_account_id=account_filtered.id,
                    category=MovementCategories.WITHDRAW_MONEY.value,
                    balance=account_filtered.funds_amount,
                    delta_amount=command.withdraw_amount,
                    concept=command.concept,
                    target_account_id=None
                )
                self.historic_movement_repository.save_movement(historic_movement)
                self.account_repository.save_account(account_filtered)
