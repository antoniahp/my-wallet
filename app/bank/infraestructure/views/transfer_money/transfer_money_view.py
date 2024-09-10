import json
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pydantic import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from bank.application.transfer_money.transfer_money_command import TransferMoneyCommand
from bank.application.transfer_money.transfer_money_command_handler import TransferMoneyCommandHandler
from bank.domain.historic_movement_creator import HistoricMovementCreator
from bank.infraestructure.db_account_repository import DbAccountRepository
from bank.infraestructure.db_historic_movemen_repository import DbHistoricMovementRepository
from bank.infraestructure.views.transfer_money.transfer_money_schema import TransferMoneySchema

@method_decorator(csrf_exempt, name="dispatch")
class TransferMoneyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.__db_account_repository = DbAccountRepository()
        self.__db_historic_movement_repository = DbHistoricMovementRepository()
        self.__historic_movement_creator = HistoricMovementCreator()
        self.__transfer_money_command_handler = TransferMoneyCommandHandler(account_repository=self.__db_account_repository, historic_movement_repository=self.__db_historic_movement_repository, historic_movement_creator=self.__historic_movement_creator)

    def post(self, request):
        request_body = json.loads(request.body)
        try:
            transfer_money_schema = TransferMoneySchema(**request_body)
        except ValidationError as e:
            print(e.json())
            return JsonResponse({'error': 'Schema error', 'details': e.json()}, status=400)
        id=uuid4()
        command = TransferMoneyCommand(
            historic_movement_id=id,
            user_id=request.user.id,
            sender_account_id=transfer_money_schema.source_account,
            recipient_account_id=transfer_money_schema.target_account,
            amount_to_send=transfer_money_schema.amount_to_send,
            concept=transfer_money_schema.concept

        )
        self.__transfer_money_command_handler.handle(command)
        return JsonResponse({'message': 'Transferencia realizada correctamente'}, status=200)
