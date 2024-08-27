from django.db import models

class MovementCategories(models.TextChoices):
    TRANSFER = 'transfer'
    DEPOSIT_MONEY = 'deposit_money'
    WITHDRAW_MONEY = 'withdraw_money'
