class RecipientAccountNotFoundException(Exception):
    def __init__(self, recipient_account_number:str):
        self.recipient_account_number = recipient_account_number
        self.message = f"Account {recipient_account_number} not found"