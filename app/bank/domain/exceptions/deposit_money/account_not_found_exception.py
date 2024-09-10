from uuid import UUID


class AccountNotFoundException(Exception):
    def __init__(self, source_account: UUID):
        self.source_account = source_account
        self.message = f"Account {source_account} not found"
        super().__init__(self.message)