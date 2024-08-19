import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from bank.application.withdraw_money.withdraw_money_command import WithdrawAmountCommand
from bank.application.withdraw_money.withdraw_money_command_handler import WithdrawMoneyCommandHandler
from bank.domain.account import Account
from bank.infraestructure.db_account_repository import DbAccountRepository
from pydantic import ValidationError

from bank.infraestructure.views.withdraw_money.withdraw_money_schema import WithdrawMoneySchema


@method_decorator(csrf_exempt, name="dispatch")
class WithdrawMoneyView(View):
    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__withdraw_money_command_handler = WithdrawMoneyCommandHandler( account_repository=self.__db_account_repository)


    def post(self, request):
        request_body = json.loads(request.body)

        try:
            withdraw_money_schema = WithdrawMoneySchema(**request_body)
        except ValidationError as e:
            print(e.json())
            return JsonResponse({'error': 'Schema error', 'details': e.json()}, status=400)


        command = WithdrawAmountCommand(
            account_number=withdraw_money_schema.account_number,
            withdraw_amount=withdraw_money_schema.withdraw_amount,
            user_id=withdraw_money_schema.user_id

        )
        self.__withdraw_money_command_handler.handle(command)

        funds_amount = Account.objects.get(account_number=withdraw_money_schema.account_number).funds_amount
        return JsonResponse({'message': f'Su saldo es de {funds_amount}€'}, status=200)
