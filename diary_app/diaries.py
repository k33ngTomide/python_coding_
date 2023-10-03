from diary_app.diary import Diary
from diary_app.exceptions_list import *
from diary_app.registered import *


class Diaries:

    def __init__(self):
        self.__list_of_diaries = []

    def add(self, username, password):
        self.__validate_username(username)
        diary = Diary(username, password)
        self.__list_of_diaries.append(diary)
        # register_user(username, password)

    def get_size(self):
        return len(self.__list_of_diaries)

    def find_by_username(self, username) -> Diary:
        for diary in self.__list_of_diaries:
            if diary.get_username() == username:
                return diary
        raise DiaryNotFoundException("Diary not found")

    def __validate_username(self, username: str):
        for diary in self.__list_of_diaries:
            if diary.get_username() == username:
                raise (UsernameExistsException
                       ("Not successful, Username already exists, try again"))

        if not username.strip() or username.isspace() or username.startswith(" "):
            raise ValueError("Username cannot be empty or start with space, try again!")

    def delete(self, username, password):
        entry = self.find_by_username(username)
        entry.validate_password(password)
        self.__list_of_diaries.remove(entry)
