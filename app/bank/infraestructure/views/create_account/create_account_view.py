import json
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bank.application.create_account.create_account_command import CreateAccountCommand
from bank.application.create_account.create_account_command_handler import CreateAccountCommandHandler
from bank.domain.account_creator import AccountCreator
from bank.infraestructure.db_account_repository import DbAccountRepository
from bank.infraestructure.db_user_repository import DbUserRepository
from bank.infraestructure.views.create_account.create_account_schema import CreateAccountSchema
from pydantic import ValidationError




@method_decorator(csrf_exempt, name="dispatch")
class CreateAccountView(View):
    def __init__(self):
        super().__init__()
        self.__db_user_repository = DbUserRepository()
        self.__db_account_repository = DbAccountRepository()
        self.__account_creator = AccountCreator(account_repository=self.__db_account_repository)
        self.__create_account_command_handler = CreateAccountCommandHandler(user_repository=self.__db_user_repository, account_creator=self.__account_creator, account_repository=self.__db_account_repository)


    def post(self, request):
        request_body = json.loads(request.body)

        try:
            create_account_schema = CreateAccountSchema(**request_body)
        except ValidationError as e:
            print(e.json())
            # Retornar una respuesta de error si la validación falla
            return JsonResponse({'error': 'Schema Error', 'details': e.json()}, status=400)


        id = uuid4()
        command = CreateAccountCommand(
            account_id=id,
            user_id=create_account_schema.user_id,
            identification_number=create_account_schema.identification_number,
            account_number=create_account_schema.account_number,
            funds_amount=create_account_schema.funds_amount,

        )
        self.__create_account_command_handler.handle(command)
        return JsonResponse({'id': str(id)}, status=201)