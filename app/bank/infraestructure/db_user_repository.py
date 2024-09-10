from typing import Optional
from bank.domain.user import User
from bank.domain.user_repository import UserRepository


class DbUserRepository(UserRepository):
    def get_user_by_identification_number(self, identification_number: str) -> Optional[User]:
        return User.objects.filter(identification_number=identification_number).first()


    def save_user(self, user: User) -> None:
        user.save()
