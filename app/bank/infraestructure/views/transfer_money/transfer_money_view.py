import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError

from bank.application.transfer_money.transfer_money_command import TransferMoneyCommand
from bank.application.transfer_money.transfer_money_command_handler import TransferMoneyCommandHandler
from bank.infraestructure.db_account_repository import DbAccountRepository
from bank.infraestructure.views.transfer_money.transfer_money_schema import TransferMoneySchema

@method_decorator(csrf_exempt, name="dispatch")
class TransferMoneyView(View):
    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__transfer_money_command_handler = TransferMoneyCommandHandler(account_repository=self.__db_account_repository)

    def post(self, request):
        request_body = json.loads(request.body)
        try:
            transfer_money_schema = TransferMoneySchema(**request_body)
        except ValidationError as e:
            print(e.json())
            return JsonResponse({'error': 'Schema error', 'details': e.json()}, status=400)

        command = TransferMoneyCommand(
            sender_account_number=transfer_money_schema.sender_account_number,
            recipient_account_number=transfer_money_schema.recipient_account_number,
            amount_to_send=transfer_money_schema.amount_to_send

        )
        self.__transfer_money_command_handler.handle(command)
        return JsonResponse({'message': 'Transferencia realizada correctamente'}, status=200)

