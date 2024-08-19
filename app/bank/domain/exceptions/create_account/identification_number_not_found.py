class IdentificationNumberNotFoundException(Exception):
    def __init__(self, identification_number: str) -> None:
        self.identification_number = identification_number
        self.message = f"This identification_number {identification_number} does not exist."
        super().__init__(self.message)