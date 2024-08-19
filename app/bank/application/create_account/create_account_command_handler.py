from bank.application.create_account.create_account_command import CreateAccountCommand
from bank.domain.account_creator import AccountCreator
from bank.domain.account_repository import AccountRepository
from bank.domain.exceptions.create_account.identification_number_not_found import IdentificationNumberNotFoundException
from bank.domain.user_repository import UserRepository


class CreateAccountCommandHandler:
    def __init__(self, account_repository:AccountRepository, account_creator:AccountCreator, user_repository:UserRepository):
        self.account_repository = account_repository
        self.account_creator = account_creator
        self.user_repository = user_repository


    def handle(self, command:CreateAccountCommand):
        user_filtered = self.user_repository.get_user_by_identification_number(identification_number=command.identification_number)
        if user_filtered is None:
            raise IdentificationNumberNotFoundException(command.identification_number)

        if user_filtered is not None:
            account_created=self.account_creator.create(
                user_id=user_filtered.id,
                account_number=command.account_number,
                funds_amount=command.funds_amount,
            )
            self.account_repository.save_account(account_created)