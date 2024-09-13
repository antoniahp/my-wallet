from datetime import date
from typing import Optional

from django.db.models import Q

from bank.domain.commissions_calculated import CommissionsCalculated
from bank.domain.commissions_calculated_repository import CommissionsCalculatedRepository


class DbCommissionsCalculatedRepository(CommissionsCalculatedRepository):

    def filter_commissions(self, country: Optional[str] = None, date__lte: Optional[date] = None, date__gte: Optional[date] = None):
        filters = Q()
        if country is not None:
            filters = filters & Q(country=country)
        if date__lte is not None:
            filters = filters & Q(date__lte=date__lte)
        if date__gte is not None:
            filters = filters & Q(date__gte=date__gte)


        commissions = CommissionsCalculated.objects.filter(filters)
        return commissions
    def save_commissions_calculated(self, commissions_calculated: CommissionsCalculated) -> None:
        commissions_calculated.save()