from datetime import date
from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    name: str
    surname: str
    born_date: date
    email: str
    phone: str
    identification_number: str