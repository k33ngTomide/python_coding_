class DiaryNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EntryNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class LockedDiaryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class UsernameExistsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectPasswordException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class SecurityNumberException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
