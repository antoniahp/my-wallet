class AccountAlreadyExists(Exception):
    def __init__(self, account_number) -> None:
        self.account_number = account_number
        self.message = f"Account with {account_number} account number already exists"
        super().__init__(self.message)