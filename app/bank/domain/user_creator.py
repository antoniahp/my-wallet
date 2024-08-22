from datetime import date

from bank.domain.exceptions.create_user.user_already_exists_exception import UserAlreadyExistsException
from bank.domain.user import User
from bank.domain.user_repository import UserRepository


class UserCreator:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository
    def create(self, name: str, surname:str, born_date: date, email:str, phone: str, identification_number: str, username: str, hashed_password: str):
        user_exists = self._user_repository.get_user_by_identification_number(identification_number=identification_number)
        if user_exists is not None:
            raise UserAlreadyExistsException(identification_number=identification_number)

        return User(
            name=name,
            surname=surname,
            born_date=born_date,
            email=email,
            phone=phone,
            identification_number=identification_number,
            username=username,
            password=hashed_password
        )
