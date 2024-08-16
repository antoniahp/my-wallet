from django.urls import path

from bank.infraestructure.views.create_account.create_account_view import CreateAccountView
from bank.infraestructure.views.create_user.create_user_view import CreateUserView
from bank.infraestructure.views.deposit_money.deposit_money_view import DepositMoneyView
from bank.infraestructure.views.transfer_money.transfer_money_view import TransferMoneyView
from bank.infraestructure.views.withdraw_money.withdraw_money import WithdrawMoneyView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='users' ),
    path('accounts/', CreateAccountView.as_view(), name='account'),
    path('withdraw_money/', WithdrawMoneyView.as_view(), name='withdraw_money'),
    path('deposit_money/', DepositMoneyView.as_view(), name='deposit_money'),
    path('transfer_money/', TransferMoneyView.as_view(), name='transfer_money'),

]