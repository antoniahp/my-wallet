from bank.application.get_filtered_commissions_calculated.get_filtered_commissions_calculated_query import GetFilteredCommissionsCalculatedQuery
from bank.domain.commissions_calculated_repository import CommissionsCalculatedRepository
from cqrs.queries.query_handler import QueryHandler
from cqrs.queries.query_response import QueryResponse


class GetFilteredCommissionsCalculatedQueryHandler(QueryHandler):
    def __init__(self, commissions_calculated_repository: CommissionsCalculatedRepository):
        self.__commissions_calculated_repository = commissions_calculated_repository

    def handle(self, query: GetFilteredCommissionsCalculatedQuery) -> QueryResponse:
        commissions = self.__commissions_calculated_repository.filter_commissions(date__lte=query.date__lte, date__gte=query.date__gte)
        return QueryResponse(content=commissions)
