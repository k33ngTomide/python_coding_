class WrongPinException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class NegativeAmountException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class InsufficientFundException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class AccountNotFoundException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class IncorrectNameException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
