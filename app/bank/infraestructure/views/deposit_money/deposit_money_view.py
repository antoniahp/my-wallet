import json
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from bank.application.deposit_money.deposit_money_command import DepositAmountCommand
from bank.application.deposit_money.deposit_money_command_handler import DepositMoneyCommandHandler
from bank.domain.account import Account
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.infraestructure.db_account_repository import DbAccountRepository
from pydantic import ValidationError

from bank.infraestructure.db_historic_movemen_repository import DbHistoricMovementRepository
from bank.infraestructure.views.deposit_money.deposit_money_schema import DepositMoneySchema


@method_decorator(csrf_exempt, name="dispatch")
class DepositMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__db_historic_movement_repository = DbHistoricMovementRepository()
        self.__historic_movement_creator = HistoricMovementCreator()
        self.__deposit_money_command_handler = DepositMoneyCommandHandler( account_repository=self.__db_account_repository, historic_movement_repository=self.__db_historic_movement_repository, historic_movement_creator=self.__historic_movement_creator)


    def post(self, request):
        request_body = json.loads(request.body)

        try:
            deposit_money_schema=DepositMoneySchema(**request_body)
        except ValidationError as e:
            print(e.json())
            return JsonResponse({'error': 'Schema error', 'details': e.json()}, status=400)

        id = uuid4()
        command = DepositAmountCommand(
            historic_movement_id=id,
            source_account=deposit_money_schema.source_account,
            deposit_amount=deposit_money_schema.deposit_amount,
            user_id=request.user.id,
            concept=deposit_money_schema.concept
        )
        self.__deposit_money_command_handler.handle(command)

        funds_amount = Account.objects.get(id=deposit_money_schema.source_account).funds_amount
        return JsonResponse({'message': f'Su saldo es de {funds_amount}€'}, status=200)
