
class AccountHasNoMovementsException(Exception):

    def __init__(self):
        self.message = f"Account has no movements"
        super().__init__(self.message)