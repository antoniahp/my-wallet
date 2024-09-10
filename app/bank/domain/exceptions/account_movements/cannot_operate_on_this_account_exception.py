from uuid import UUID


class CanNotOperateOnThisAccountException(Exception):
    def __init__(self):
        self.message = f"You cannot operate on this account"
        super().__init__()