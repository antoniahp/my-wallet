from datetime import date
from unicodedata import decimal

from bank.domain.calculated_commissions import CalculatedCommissions


class CalculatedCommissionsCreator:

    def create(self, date: date, country: str, total_amount_commission: decimal) -> CalculatedCommissions:
        return CalculatedCommissions(
            date=date,
            country=country,
            total_amount_commission=total_amount_commission
        )