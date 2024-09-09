import json
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from bank.application.withdraw_money.withdraw_money_command import WithdrawAmountCommand
from bank.application.withdraw_money.withdraw_money_command_handler import WithdrawMoneyCommandHandler
from bank.domain.account import Account
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.infraestructure.db_account_repository import DbAccountRepository
from pydantic import ValidationError

from bank.infraestructure.db_historic_movemen_repository import DbHistoricMovementRepository
from bank.infraestructure.views.withdraw_money.withdraw_money_schema import WithdrawMoneySchema


@method_decorator(csrf_exempt, name="dispatch")
class WithdrawMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__db_historic_movement_repository = DbHistoricMovementRepository()
        self.__historic_movement_creator = HistoricMovementCreator()
        self.__withdraw_money_command_handler = WithdrawMoneyCommandHandler( account_repository=self.__db_account_repository, historic_movement_repository=self.__db_historic_movement_repository, historic_movement_creator=self.__historic_movement_creator)


    def post(self, request):
        request_body = json.loads(request.body)

        try:
            withdraw_money_schema = WithdrawMoneySchema(**request_body)
        except ValidationError as e:
            print(e.json())
            return JsonResponse({'error': 'Schema error', 'details': e.json()}, status=400)

        id = uuid4()
        command = WithdrawAmountCommand(
            historic_movement_id=id,
            source_account=withdraw_money_schema.source_account,
            withdraw_amount=withdraw_money_schema.withdraw_amount,
            user_id=request.user.id,
            concept=withdraw_money_schema.concept

        )
        self.__withdraw_money_command_handler.handle(command)

        funds_amount = Account.objects.get(id=withdraw_money_schema.source_account).funds_amount
        return JsonResponse({'message': f'Su saldo es de {funds_amount}€'}, status=200)
