from dataclasses import dataclass
from datetime import date
from uuid import UUID
from cqrs.commands.command import Command


@dataclass(frozen=True)
class CreateUserCommand(Command):
    id: UUID
    name: str
    surname: str
    born_date: date
    email: str
    phone: str
    identification_number: str
    username: str
    hashed_password: str
