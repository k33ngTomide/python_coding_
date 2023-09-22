import unittest

from contact_log_app.contact import Contact
from contact_log_app.contact_log_impl import ContactLogImpl


class ContactLogImplTest(unittest.TestCase):

    def setUp(self):
        self.contact_log = ContactLogImpl()

    def test_save_contact_increases_count(self):
        contact = Contact()
        self.contact_log.save(contact)
        self.assertEqual(1, self.contact_log.count())

    def test_save_contact_find_contact(self):
        contact = Contact()
        self.contact_log.save(contact)
        self.assertEqual(contact, self.contact_log.find_by_id(contact.get_contact_id()))

    def test_update_contact(self):
        contact = Contact()
        contact.set_name("Muiliyu Sodiq")
        self.contact_log.save(contact)

        new_contact = Contact()
        new_contact.set_contact_id(1)
        new_contact.set_address("Sabo Yaba")
        new_contact.set_email("Nothing@gmail.com")
        new_contact.set_name("Nothing Ham")
        new_contact.set_telephone("081010101")
        self.contact_log.save(new_contact)

        self.assertEqual(new_contact, self.contact_log.find_by_id(contact.get_contact_id()))

    def test_add_more_contacts_increases_count(self):
        contact = Contact()
        self.contact_log.save(contact)

        new_contact = Contact()
        self.contact_log.save(new_contact)

        self.assertEqual(2, self.contact_log.count())

        another_contact = Contact()
        self.contact_log.save(another_contact)
        self.assertEqual(3, self.contact_log.count())

    def test_find_contact_by_id_returns_none_if_contact_id_does_not_exist(self):
        contact = Contact()
        self.contact_log.save(contact)
        self.assertIsNone(self.contact_log.find_by_id(2))

    def test_delete_contact_decreases_count(self):
        contact = Contact()
        new_contact = Contact()
        self.contact_log.save(contact)
        self.contact_log.save(new_contact)
        self.assertEqual(2, self.contact_log.count())

        self.contact_log.delete(contact)
        self.assertEqual(1, self.contact_log.count())

    def test_delete_contact_removes_contact_returns_none(self):
        contact = Contact()
        new_contact = Contact()
        self.contact_log.save(contact)
        self.contact_log.save(new_contact)
        self.assertEqual(2, self.contact_log.count())

        self.contact_log.delete(contact)
        self.assertIsNone(self.contact_log.find_by_id(contact.get_contact_id()))

    def test_find_all(self):
        contact = Contact()
        self.contact_log.save(contact)

        new_contact = Contact()
        self.contact_log.save(new_contact)

        another_contact = Contact()
        self.contact_log.save(another_contact)

        contact_iterable = [contact, new_contact, another_contact]
        self.assertListEqual(contact_iterable, list(self.contact_log.find_all()))

    def test_clear_returns_count_to_zero(self):
        contact = Contact()
        self.contact_log.save(contact)

        new_contact = Contact()
        self.contact_log.save(new_contact)

        another_contact = Contact()
        self.contact_log.save(another_contact)
        self.assertEqual(3, self.contact_log.count())

        self.contact_log.clear()
        self.assertEqual(0, self.contact_log.count())

    def test_clear_removes_all_contacts(self):
        contact = Contact()
        self.contact_log.save(contact)

        new_contact = Contact()
        self.contact_log.save(new_contact)

        another_contact = Contact()
        self.contact_log.save(another_contact)
        self.assertEqual(3, self.contact_log.count())

        self.contact_log.clear()
        self.assertIsNone(self.contact_log.find_by_id(contact.get_contact_id()))
        self.assertIsNone(self.contact_log.find_by_id(new_contact.get_contact_id()))
        self.assertIsNone(self.contact_log.find_by_id(another_contact.get_contact_id()))


if __name__ == '__main__':
    unittest.main()
