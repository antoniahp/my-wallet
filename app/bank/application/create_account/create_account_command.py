from uuid import UUID
from dataclasses import dataclass
from decimal import Decimal

from cqrs.commands.command import Command


@dataclass(frozen=True)
class CreateAccountCommand(Command):
    user_id: UUID
    identification_number: str
    account_id: UUID
    account_number: str
    funds_amount: Decimal
