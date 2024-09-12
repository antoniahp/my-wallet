import uuid

from django.db import models

from bank.domain.commisions_by_country_choices import CommissionsByCountryChoices


class CommissionsByCountry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    country = models.CharField(max_length=20, choices=CommissionsByCountryChoices.choices)
    commission_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    range_min = models.IntegerField()
    range_max = models.IntegerField()

