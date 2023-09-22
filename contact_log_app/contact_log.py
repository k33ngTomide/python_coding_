from abc import ABC, abstractmethod


class ContactLog(ABC):
    @abstractmethod
    def save(self, contact):
        pass

    @abstractmethod
    def find_by_id(self, contact_id):
        pass

    @abstractmethod
    def delete(self, contact):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def count(self):
        pass
