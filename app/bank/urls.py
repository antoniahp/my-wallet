from django.urls import path

from bank.infraestructure.views.create_account.create_account_view import CreateAccountView
from bank.infraestructure.views.create_user.create_user_view import CreateUserView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='users' ),
    path('accounts/', CreateAccountView.as_view(), name='account' )
]