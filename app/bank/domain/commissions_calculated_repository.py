from abc import ABC, abstractmethod

from bank.domain.commissions_calculated import CommissionsCalculated


class CommissionsCalculatedRepository(ABC):
    @abstractmethod
    def save_commissions_calculated(self, commissions_calculated: CommissionsCalculated) -> None:
        pass