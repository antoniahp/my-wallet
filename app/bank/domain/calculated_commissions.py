import uuid
from datetime import date
from django.db import models

from bank.domain.commisions_by_country_choices import CommissionsByCountryChoices


class CalculatedCommissions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField("Date", default=date.today)
    country = models.CharField(max_length=20, choices=CommissionsByCountryChoices.choices)
    total_amount_commission = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.country}.{self.total_amount_commission}"