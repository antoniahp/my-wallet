import json
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bank.application.create_user.create_user_command import CreateUserCommand
from bank.application.create_user.create_user_command_handler import CreateUserCommandHandler
from bank.domain.exceptions.create_user.user_already_exists import UserAlreadyExists
from bank.domain.user_creator import UserCreator
from bank.infraestructure.db_user_repository import DbUserRepository
from bank.infraestructure.views.create_user.create_user_schema import CreateUserSchema
from pydantic import ValidationError




@method_decorator(csrf_exempt, name="dispatch")
class CreateUserView(View):
    def __init__(self):
        super().__init__()
        self.__db_user_repository = DbUserRepository()
        self.__user_creator = UserCreator(user_repository=self.__db_user_repository)
        self.__create_user_command_handler = CreateUserCommandHandler(user_repository=self.__db_user_repository, user_creator=self.__user_creator)


    def post(self, request):
        request_body = json.loads(request.body)

        try:
            create_user_schema = CreateUserSchema(**request_body)
        except ValidationError as e:
            print(e.json())
            # Retornar una respuesta de error si la validación falla
            return JsonResponse({'error': 'Invalid input', 'details': e.json()}, status=400)


        id = uuid4()
        command = CreateUserCommand(
            id=id,
            name=create_user_schema.name,
            surname=create_user_schema.surname,
            born_date=create_user_schema.born_date,
            email=create_user_schema.email,
            phone=create_user_schema.phone,
            identification_number=create_user_schema.identification_number,

        )
        try:
            self.__create_user_command_handler.handle(command)
            return JsonResponse({'id': str(id)}, status=201)

        except UserAlreadyExists:
            return JsonResponse({'Error': "You can't create a user with his identification number"}, status=400)

        except Exception:
            return JsonResponse({'Error': "server error"}, status=500)