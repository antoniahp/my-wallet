import uuid
from datetime import date

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    born_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    identification_number = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def calculate_age(self):
        today = date.today()
        age = today.year - self.born_date.year
        if today < date(today.year, self.born_date.month, self.born_date.day):
            age -= 1
        return age