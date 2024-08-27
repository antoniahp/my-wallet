from abc import abstractmethod, ABC

from bank.domain.historic_movement import HistoricMovement


class HistoricMovementRepository(ABC):
    @abstractmethod
    def save_movement(self, historic_movement: HistoricMovement) -> None:
        pass