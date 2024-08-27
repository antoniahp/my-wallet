from decimal import Decimal
from typing import Optional
from uuid import UUID

from bank.domain.historic_movement import HistoricMovement
from bank.domain.historic_movement_repository import HistoricMovementRepository


class HistoricMovementCreator:

    def create(self, user_account_number: UUID, category: str, balance: Decimal, delta_amount: Decimal, concept: str, recipient: Optional[UUID]):
        return HistoricMovement(
            user_account_number=user_account_number,
            category=category,
            balance=balance,
            delta_amount=delta_amount,
            concept=concept,
            recipient=recipient
        )