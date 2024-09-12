from dataclasses import dataclass
from typing import Optional
from datetime import date

from cqrs.commands.command import Command

@dataclass(frozen=True)
class CalculatedCommissionsCommand(Command):
    country: str
    date: date