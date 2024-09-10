from uuid import UUID


class RecipientAccountNotFoundException(Exception):
    def __init__(self, recipient_account_number:UUID):
        self.recipient_account_number = recipient_account_number
        self.message = f"Account {recipient_account_number} not found"