import uuid
from django.db import models
from bank.domain.user import User


class AccountNumber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account_number = models.CharField(max_length=50, unique=True)
    funds_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number
