class AccountNotFoundException(Exception):
    def __init__(self, account_number:str):
        self.account_number = account_number
        self.message = f"Account {account_number} not found"