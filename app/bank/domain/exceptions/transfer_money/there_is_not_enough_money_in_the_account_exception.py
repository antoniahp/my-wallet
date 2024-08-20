class ThereIsNotEnoughMoneyInTheAccountException(Exception):
    def __init__(self) -> None:
        self.message = "There is not enough money in the account"
        super().__init__(self.message)