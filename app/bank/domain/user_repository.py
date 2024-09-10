from abc import abstractmethod, ABC
from typing import Optional
from bank.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_identification_number(self, identification_number: str) -> Optional[User]:
        pass

    @abstractmethod
    def save_user(self, user: User) -> None:
        pass
