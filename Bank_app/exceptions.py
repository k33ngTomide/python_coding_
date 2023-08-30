
class WrongPinException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class NegativeAmountException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class InsufficientFundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class AccountNotFoundException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
