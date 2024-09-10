from datetime import datetime
from typing import Optional
from uuid import UUID

from django.db.models import Q

from bank.domain.historic_movement import HistoricMovement
from bank.domain.historic_movement_repository import HistoricMovementRepository


class DbHistoricMovementRepository(HistoricMovementRepository):
    def filter_movement(self, source_account:Optional[UUID] = None, created_at:Optional[datetime] = None):
        filters = Q()
        if source_account is not None:
            filters = filters & Q(source_account=source_account)
        if created_at is not None:
            filters = filters & Q(created_at__gte=created_at)

        movements = HistoricMovement.objects.filter(filters).order_by("-created_at")
        return movements

    def save_movement(self, historic_movement: HistoricMovement) -> None:
        historic_movement.save()
