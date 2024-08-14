from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(frozen=True)
class CreateUserCommand:
    id: UUID
    name: str
    surname: str
    born_date: date
    email: str
    phone: str
    identification_number: str
