from dataclasses import dataclass
from datetime import date

from cqrs.commands.command import Command


@dataclass(frozen=True)
class CommissionCalculatedCommand(Command):
    hours_commission_calculated: int
    date: date

