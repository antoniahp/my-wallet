from decimal import Decimal
from typing import Optional
from uuid import UUID

from bank.domain.historic_movement import HistoricMovement


class HistoricMovementCreator:

    def create(self, source_account_id: UUID, category: str, balance: Decimal, delta_amount: Decimal, concept: Optional[str], target_account_id: Optional[UUID], commission: Optional[Decimal], country:Optional[str]):
        return HistoricMovement(
            source_account_id=source_account_id,
            category=category,
            balance=balance,
            delta_amount=delta_amount,
            country=country,
            commission=commission,
            concept=concept,
            target_account_id=target_account_id
        )
