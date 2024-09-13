from django.contrib import admin
from bank.domain.account import Account
from bank.domain.commissions_by_country import CommissionsByCountry
from bank.domain.commissions_calculated import CommissionsCalculated
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

class CommissionsCalculatedAdmin(admin.ModelAdmin):
    list_display = [
        'country',
        'date',
        'total_amount_commission'
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(HistoricMovement, HistoricMovementAdmin)
admin.site.register(CommissionsByCountry, CommissionsByCountryAdmin)
admin.site.register(CommissionsCalculated,CommissionsCalculatedAdmin)