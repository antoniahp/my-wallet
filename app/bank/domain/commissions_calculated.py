import uuid

from django.db import models

from bank.domain.commisions_by_country_choices import CommissionsByCountryChoices


class CommissionsCalculated(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    country = models.CharField(max_length=20, choices=CommissionsByCountryChoices.choices)
    date = models.DateTimeField()
    total_amount_commission = models.DecimalField(max_digits=10, decimal_places=2)
