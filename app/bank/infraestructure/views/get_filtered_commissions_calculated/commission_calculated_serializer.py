from decimal import Decimal
from typing import List

from bank.domain.commissions_calculated import CommissionsCalculated


class CommissionCalculatedSerializer:
    def serialize(self, commissions: List[CommissionsCalculated]) -> dict :
        commissions_list = []
        total = 0
        for commission in commissions:
            total = total + commission.total_amount_commission
            commissions_list.append({
                "id": commission.id,
                "country": commission.country,
                "date": commission.date,
                "total_amount_commission": float(commission.total_amount_commission),
            })

        return {
            "commissions": commissions_list,
            "total": float(total)

        }