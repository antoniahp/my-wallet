from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional
from uuid import UUID


from bank.domain.historic_movement import HistoricMovement


class HistoricMovementRepository(ABC):
    @abstractmethod
    def filter_movements(self, country: Optional[str] = None, created_at__lte: Optional[datetime] = None,  created_at__gte: Optional[datetime] = None, source_account:Optional[UUID] = None, created_at:Optional[datetime] = None):
        pass


    @abstractmethod
    def save_movement(self, historic_movement: HistoricMovement) -> None:
        pass
