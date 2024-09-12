from abc import ABC, abstractmethod
from typing import Optional

from django.db.models import Q

from bank.domain.commissions_by_country import CommissionsByCountry
from bank.domain.commissions_by_country_repository import CommissionsByCountryRepository


class DbCommissionsByCountryRepository(CommissionsByCountryRepository):
    def filter_commissions(self, country: Optional [str] = None, range_min_lte: Optional [int] = None, range_max_gte:Optional [int] = None):
        filters = Q()
        if country is not None:
            filters = filters & Q(country=country)
        if range_min_lte is not None:
            filters = filters & Q(range_min__lte=range_min_lte)
        if range_max_gte is not None:
            filters = filters & Q(range_max__gte=range_max_gte)

        commissions = CommissionsByCountry.objects.filter(filters).first()
        return commissions
