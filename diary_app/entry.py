import datetime


class Entry:

    def __init__(self, id, title, body):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__date_created = datetime.datetime.now()

    def get_entry_id(self) -> int:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    def get_entry_details(self) -> str:
        return (f"Entry id: {self.__id}"
                f"\nTitle: {self.__title} "
                f"\nContent: {self.__body}"
                f"\nDate Created: {self.__date_created} ")


