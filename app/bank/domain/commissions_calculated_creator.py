from datetime import date
from unicodedata import decimal

from bank.domain.commissions_calculated import CommissionsCalculated


class CommissionsCalculatedCreator:
    def create(self, country: str, date: date, total_amount_commission: decimal):
        return CommissionsCalculated(
            country=country,
            date=date,
            total_amount_commission=total_amount_commission,
        )