from bank.domain.commissions_calculated import CommissionsCalculated
from bank.domain.commissions_calculated_repository import CommissionsCalculatedRepository


class DbCommissionsCalculatedRepository(CommissionsCalculatedRepository):

    def save_commissions_calculated(self, commissions_calculated: CommissionsCalculated) -> None:
        commissions_calculated.save()