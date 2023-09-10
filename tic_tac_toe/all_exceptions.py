class InvalidPlayerException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidMoveException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidInputException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
