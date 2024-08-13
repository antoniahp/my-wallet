import uuid
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CreateUserCommand:
    id: uuid
    name: str
    surname: str
    born_date: date
    email: str
    phone: str
    identification_number: str
    created_at: date