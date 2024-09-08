from decimal import Decimal
from typing import Optional
from uuid import UUID

from bank.domain.historic_movement import HistoricMovement
from bank.domain.historic_movement_repository import HistoricMovementRepository


class HistoricMovementCreator:

    def create(self, source_account_id: UUID, category: str, balance: Decimal, delta_amount: Decimal, concept: Optional[str], target_account: Optional[UUID]):
        return HistoricMovement(
            source_account_id=source_account_id,
            category=category,
            balance=balance,
            delta_amount=delta_amount,
            concept=concept,
            target_account=target_account
        )