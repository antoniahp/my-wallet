class UserAlreadyExists(Exception):
    def __init__(self, identification_number) -> None:
        self.account_number = identification_number
        self.message = f"User with identification number {identification_number}  already exists"
        super().__init__(self.message)