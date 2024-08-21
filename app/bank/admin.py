from django.contrib import admin
from bank.domain.account import Account
from bank.domain.user import User



class UserAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'surname',
    ]
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'account_number',
        'funds_amount',
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
