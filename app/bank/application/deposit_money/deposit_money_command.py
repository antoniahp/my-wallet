from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID
from cqrs.commands.command import Command


@dataclass(frozen=True)
class DepositAmountCommand(Command):
    historic_movement_id: UUID
    user_id: UUID
    deposit_amount: Decimal
    concept: str
    source_account: UUID
