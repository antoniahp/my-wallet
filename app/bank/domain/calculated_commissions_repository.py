from abc import ABC, abstractmethod

from bank.domain.calculated_commissions import CalculatedCommissions


class CalculatedCommissionsRepository(ABC):
    @abstractmethod
    def save_calculated_commissions(self, calculated_commissions:CalculatedCommissions) -> None:
        pass