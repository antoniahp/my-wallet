from datetime import datetime

from django.http import JsonResponse
from django.views import View

from bank.application.get_filtered_commissions_calculated.get_filtered_commissions_calculated_query import GetFilteredCommissionsCalculatedQuery
from bank.application.get_filtered_commissions_calculated.get_filtered_commissions_calculated_query_handler import GetFilteredCommissionsCalculatedQueryHandler
from bank.infraestructure.db_commissions_calculated_repository import DbCommissionsCalculatedRepository
from bank.infraestructure.views.get_filtered_commissions_calculated.commission_calculated_serializer import CommissionCalculatedSerializer


class FilteredCommissionsCalculatedView(View):
    def __init__(self):
        self.__db_commissions_calculated_repository = DbCommissionsCalculatedRepository()
        self.__get_filtered_commissions_calculated_query_handler = GetFilteredCommissionsCalculatedQueryHandler(commissions_calculated_repository=self.__db_commissions_calculated_repository)
        self.__commissions_calculated_serialize = CommissionCalculatedSerializer()
    def get(self, request):
        date__gte =  datetime.strptime(request.GET.get("date__gte"), "%d/%m/%Y")
        date__lte = datetime.strptime(request.GET.get("date__lte"), "%d/%m/%Y")
        query = GetFilteredCommissionsCalculatedQuery(date__gte=date__gte, date__lte=date__lte)
        query_response = self.__get_filtered_commissions_calculated_query_handler.handle(query)
        commissions = query_response.content
        return JsonResponse(
            self.__commissions_calculated_serialize.serialize(commissions),
         status=200
        )