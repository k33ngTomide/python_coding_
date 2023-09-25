from abc import ABC

from contact_log_app.contact_log import ContactLog


class ContactLogImpl(ContactLog):
    def __init__(self):
        self.contacts = []

    def save(self, contact):
        contact_does_not_exist = contact.get_contact_id() == 0
        if contact_does_not_exist:
            self.__save_new(contact)
        else:
            self.__update(contact)
        return contact

    def __save_new(self, contact):
        contact.set_contact_id(self.__generate_id())
        self.contacts.append(contact)

    def __generate_id(self):
        return len(self.contacts) + 1

    def __update(self, contact):
        old_contact = self.find_by_id(contact.get_contact_id())
        old_contact.set_telephone(contact.get_telephone())
        old_contact.set_address(contact.get_address())
        old_contact.set_name(contact.get_name())
        old_contact.set_email(contact.get_email())

    def find_by_id(self, contact_id):
        for contact in self.contacts:
            if contact.get_contact_id() == contact_id:
                return contact
        return None

    def delete(self, contact):
        found_contact = self.find_by_id(contact.get_contact_id())
        self.contacts.remove(found_contact)

    def find_all(self):
        return self.contacts

    def clear(self):
        self.contacts.clear()

    def count(self):
        return len(self.contacts)
