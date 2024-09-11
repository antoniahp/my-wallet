from django.contrib import admin
from bank.domain.account import Account
from bank.domain.commisions_by_country import CommissionsByCountry
from bank.domain.historic_movement import HistoricMovement
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

class HistoricMovementAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'delta_amount',
    ]

class CommissionsByCountryAdmin(admin.ModelAdmin):
    list_display = [
        'country',
        'range_min',
        'range_max',
        'commission_percentage'
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(HistoricMovement, HistoricMovementAdmin)
admin.site.register(CommissionsByCountry, CommissionsByCountryAdmin)
