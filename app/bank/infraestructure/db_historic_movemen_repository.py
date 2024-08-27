from bank.domain.historic_movement import HistoricMovement
from bank.domain.historic_movement_repository import HistoricMovementRepository


class DbHistoricMovementRepository(HistoricMovementRepository):

    def save_movement(self, historic_movement: HistoricMovement) -> None:
        historic_movement.save()


