import json
from datetime import datetime
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bank.application.create_user.create_user_command import CreateUserCommand
from bank.application.create_user.create_user_command_handler import CreateUserCommandHandler
from bank.domain.user_creator import UserCreator
from bank.infraestructure.db_user_repository import DbUserRepository

@method_decorator(csrf_exempt, name="dispatch")
class CreateUserView(View):
    def __init__(self):
        super().__init__()
        self.__db_user_repository = DbUserRepository()
        self.__user_creator = UserCreator()
        self.__create_user_command_handler = CreateUserCommandHandler(user_repository=self.__db_user_repository, user_creator=self.__user_creator)


    def post(self, request):
        data = json.loads(request.body)
        id = uuid4()
        command = CreateUserCommand(
            id=id,
            name=data.get("name"),
            surname=data.get("surname"),
            born_date=datetime.strptime(data.get("born_date"), "%d-%m-%Y").date(),
            email=data.get("email"),
            phone=data.get("phone"),
            identification_number=data.get("identification_number"),
            created_at=data.get("created_at"),
        )
        self.__create_user_command_handler.handle(command)
        return JsonResponse({'id': str(id)}, status=201)