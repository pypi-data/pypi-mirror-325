

class AIssociateError(Exception):
    pass


class AIssociateAPIError(AIssociateError):
    message: str

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message