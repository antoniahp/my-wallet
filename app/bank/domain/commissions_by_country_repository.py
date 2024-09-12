from abc import ABC, abstractmethod
from typing import Optional


class CommissionsByCountryRepository(ABC):
    @abstractmethod
    def filter_commissions(self, country: Optional [str] = None, range_min_lte: Optional [int] = None, range_max_gte:Optional [int] = None):
        pass