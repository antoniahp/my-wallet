from abc import ABC, abstractmethod

from bank.domain.calculated_commissions import CalculatedCommissions
from bank.domain.calculated_commissions_repository import CalculatedCommissionsRepository


class DbCalculatedCommissionsRepository(CalculatedCommissionsRepository):
    def save_calculated_commissions(self, calculated_commissions:CalculatedCommissions) -> None:
       return calculated_commissions.save()