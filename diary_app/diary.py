from diary_app.entry import *
from diary_app.exceptions_list import *


class Diary:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__is_locked = False
        self.__list_of_entry = []

    def is_locked(self) -> bool:
        return self.__is_locked

    def lock_diary(self):
        self.__is_locked = True

    def unlock_diary(self, password):
        self.validate_password(password)
        self.__is_locked = False

    def create_entry(self, title, body):
        self.validate_diary_is_not_locked()
        entry = Entry(self.__generate_entry_id(), title, body)
        self.__list_of_entry.append(entry)

    def findEntry(self, entry_id) -> Entry:
        self.validate_diary_is_not_locked()
        for entry in self.__list_of_entry:
            if entry.get_entry_id() == entry_id:
                return entry
        raise EntryNotFoundException("Entry Not Found")

    def __generate_entry_id(self) -> str:
        return str(len(self.__list_of_entry) + 1)

    def validate_diary_is_not_locked(self):
        if self.is_locked():
            raise LockedDiaryException("Diary is Locked")

    def get_number_of_entries(self):
        self.validate_diary_is_not_locked()
        return len(self.__list_of_entry)

    def delete_entry(self, entry_id):
        entry = self.findEntry(entry_id)
        self.__list_of_entry.remove(entry)

    def update_entry(self, entry_id, title, body):
        entry = self.findEntry(entry_id)
        entry.title = title
        entry.body = body

    def get_username(self):
        return self.__username

    def validate_password(self, password):
        if self.__password != password:
            raise IncorrectPasswordException("Incorrect Password")

    def view_all_entries(self) -> str:
        return "".join(
            entry.get_entry_details() + "\n\n"
            for entry in self.__list_of_entry
        )

