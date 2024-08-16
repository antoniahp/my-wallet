from django.db import transaction

from bank.application.transfer_money.transfer_money_command import TransferMoneyCommand
from bank.domain.account_repository import AccountRepository


class TransferMoneyCommandHandler:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def handle(self, command:TransferMoneyCommand):
        sender_account_filtered = self.account_repository.get_account_by_iban(account_number=command.sender_account_number)
        recipient_account_filtered = self.account_repository.get_account_by_iban(account_number=command.recipient_account_number)

        if sender_account_filtered.funds_amount >= command.amount_to_send:
            sender_account_filtered.funds_amount = sender_account_filtered.funds_amount - command.amount_to_send
            recipient_account_filtered.funds_amount = recipient_account_filtered.funds_amount + command.amount_to_send

            with transaction.atomic():
                self.account_repository.save_account(sender_account_filtered)
                self.account_repository.save_account(recipient_account_filtered)





