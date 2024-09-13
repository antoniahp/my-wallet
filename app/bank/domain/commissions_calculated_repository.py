from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

from bank.domain.commissions_calculated import CommissionsCalculated


class CommissionsCalculatedRepository(ABC):
    @abstractmethod
    def filter_commissions(self, country: Optional[str] = None, date__lte: Optional[date] = None,  date__gte: Optional[date] = None):
        pass

    @abstractmethod
    def save_commissions_calculated(self, commissions_calculated: CommissionsCalculated) -> None:
        pass