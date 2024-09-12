from decimal import Decimal

from django.db import transaction

from bank.application.transfer_money.transfer_money_command import TransferMoneyCommand
from bank.domain.account_repository import AccountRepository
from bank.domain.commisions_by_country_choices import CommissionsByCountryChoices
from bank.domain.exceptions.account_movements.cannot_operate_on_this_account_exception import CanNotOperateOnThisAccountException
from bank.domain.exceptions.transfer_money.recipient_account_not_found_exception import RecipientAccountNotFoundException
from bank.domain.exceptions.transfer_money.there_is_not_enough_money_in_the_account_exception import ThereIsNotEnoughMoneyInTheAccountException
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.domain.historic_movement_repository import HistoricMovementRepository
from bank.domain.movement_categories import MovementCategories


class TransferMoneyCommandHandler:
    def __init__(self, account_repository: AccountRepository, historic_movement_repository: HistoricMovementRepository, historic_movement_creator: HistoricMovementCreator):
        self.account_repository = account_repository
        self.historic_movement_repository = historic_movement_repository
        self.historic_movement_creator = historic_movement_creator

    def handle(self, command:TransferMoneyCommand):
        with transaction.atomic():
            sender_account_filtered = self.account_repository.get_account_by_id(source_account=command.sender_account_id, select_for_update=True)
            recipient_account_filtered = self.account_repository.get_account_by_id(source_account=command.recipient_account_id, select_for_update=True)

            if "ES" in sender_account_filtered.account_number:
                country = CommissionsByCountryChoices.SPAIN.value
            elif "PT" in sender_account_filtered.account_number:
                country = CommissionsByCountryChoices.PORTUGAL.value
            else:
                country = CommissionsByCountryChoices.FRANCE.value

            if sender_account_filtered.user_id != command.user_id:
                raise CanNotOperateOnThisAccountException()

            if recipient_account_filtered is None:
                raise RecipientAccountNotFoundException(recipient_account_number=command.recipient_account_id)


            if sender_account_filtered.funds_amount < command.amount_to_send:
                raise ThereIsNotEnoughMoneyInTheAccountException()

            sender_account_filtered.funds_amount = sender_account_filtered.funds_amount - command.amount_to_send
            recipient_account_filtered.funds_amount = recipient_account_filtered.funds_amount + command.amount_to_send


            historic_movement_sender = self.historic_movement_creator.create(
                source_account_id=sender_account_filtered.id,
                category=MovementCategories.TRANSFER.value,
                balance=sender_account_filtered.funds_amount,
                delta_amount=command.amount_to_send,
                concept=command.concept,
                target_account_id=recipient_account_filtered.id,
                commission = Decimal(0),
                country = country
            )

            historic_movement_target = self.historic_movement_creator.create(
                source_account_id=recipient_account_filtered.id,
                category=MovementCategories.DEPOSIT_MONEY.value,
                balance=recipient_account_filtered.funds_amount,
                delta_amount=command.amount_to_send,
                concept=command.concept,
                target_account_id=None
            )


            self.historic_movement_repository.save_movement(historic_movement_sender)
            self.historic_movement_repository.save_movement(historic_movement_target)


            self.account_repository.save_account(sender_account_filtered)
            self.account_repository.save_account(recipient_account_filtered)

