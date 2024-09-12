from abc import abstractmethod, ABC
from datetime import datetime, date
from typing import Optional, List
from uuid import UUID


from bank.domain.historic_movement import HistoricMovement


class HistoricMovementRepository(ABC):
    @abstractmethod
    def filter_movements(self,
                         source_account:Optional[UUID] = None,
                         created_at:Optional[datetime] = None,
                         country: Optional [str] = None,
                         date__lte: Optional [date] = None,
                         date__gte:Optional [date] = None,
                         date:Optional [date] = None
                         ) -> List[HistoricMovement]:
        pass


    @abstractmethod
    def save_movement(self, historic_movement: HistoricMovement) -> None:
        pass
