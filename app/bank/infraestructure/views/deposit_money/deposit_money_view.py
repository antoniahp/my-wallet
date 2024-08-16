import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bank.application.deposit_money.deposit_money_command import DepositAmountCommand
from bank.application.deposit_money.deposit_money_command_handler import DepositMoneyCommandHandler
from bank.domain.account import Account
from bank.infraestructure.db_account_repository import DbAccountRepository
from pydantic import ValidationError

from bank.infraestructure.views.deposit_money.deposit_money_schema import DepositMoneySchema


@method_decorator(csrf_exempt, name="dispatch")
class DepositMoneyView(View):
    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__deposit_money_command_handler = DepositMoneyCommandHandler( account_repository=self.__db_account_repository)


    def post(self, request):
        request_body = json.loads(request.body)

        try:
            deposit_money_schema=DepositMoneySchema(**request_body)
        except ValidationError as e:
            print(e.json())
            return JsonResponse({'error': 'Schema error', 'details': e.json()}, status=400)


        command = DepositAmountCommand(
            account_number=deposit_money_schema.account_number,
            deposit_amount=deposit_money_schema.deposit_amount,

        )
        self.__deposit_money_command_handler.handle(command)

        funds_amount = Account.objects.get(account_number=deposit_money_schema.account_number).funds_amount
        return JsonResponse({'message': f'Su saldo es de {funds_amount}€'}, status=200)
