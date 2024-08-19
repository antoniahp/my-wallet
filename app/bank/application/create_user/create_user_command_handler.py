from bank.application.create_user.create_user_command import CreateUserCommand
from bank.domain.user_creator import UserCreator
from bank.domain.user_repository import UserRepository


class CreateUserCommandHandler:
    def __init__(self, user_repository:UserRepository, user_creator:UserCreator):
        self.user_repository = user_repository
        self.user_creator = user_creator

    def handle(self, command:CreateUserCommand):

       user_created = self.user_creator.create(
            name=command.name,
            surname = command.surname,
            born_date = command.born_date,
            email = command.email,
            phone=command.phone,
            identification_number=command.identification_number,
        )

       self.user_repository.save_user(user_created)
