from datetime import date

from bank.domain.user import User


class UserCreator:
    def create(self, name: str, surname:str, born_date: date, email:str, phone: str, identification_number: str):
        return User(
            name=name,
            surname=surname,
            born_date=born_date,
            email=email,
            phone=phone,
            identification_number=identification_number,
            created_at=date.today()
        )