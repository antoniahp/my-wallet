from bank.domain.user import User


class UserRepository:
    @staticmethod
    def get_user_by_dni(dni: str) -> User:
        pass

    def save_user(self, user: User) -> None:
        pass