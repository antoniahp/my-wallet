from django.urls import path
from bank.infraestructure.views.create_user_view import CreateUserView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='users' )
]