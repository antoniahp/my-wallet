import uuid
from django.db import models

from bank.domain.account import Account
from bank.domain.movement_categories import MovementCategories


class HistoricMovement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    source_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="historic_movements")
    category = models.CharField(max_length=50, choices=MovementCategories.choices)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    delta_amount = models.DecimalField(max_digits=12, decimal_places=2)
    commission = models.DecimalField(max_digits=12, decimal_places=2)
    country = models.CharField(max_length=20)
    concept = models.CharField(max_length=100, null=True)
    target_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="recipient_historic_movements", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

