from django.contrib import admin

from bank.domain.account_number import AccountNumber
from bank.domain.user import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'surname',
        #'account_number',
        #'funds_amount',
    ]
class AccountNumberAdmin(admin.ModelAdmin):
    list_display = [
        'account_number',
        'funds_amount',
    ]

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(AccountNumber, AccountNumberAdmin)
