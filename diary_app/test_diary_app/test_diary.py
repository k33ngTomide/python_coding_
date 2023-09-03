import unittest

from diary_app.diary import Diary


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.diary = Diary("Username", "password")

    def test_that_diary_is_not_locked(self):
        self.assertFalse(self.diary.is_locked())

    def test_that_diary_can_be_locked(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

    def test_that_diary_can_be_unlocked(self):
        self.assertFalse(self.diary.is_locked())
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked())

        self.diary.unlock_diary()
        self.assertFalse(self.diary.is_locked())

    def test_that_diary_can_create_entry(self):
        self.assertFalse(self.diary.is_locked())

        self.diary.create_entry("title", "body")
        self.assertEqual(self.diary.findEntry(1).get_entry_id(), 1)

    def test_that_dairy_can_create_entries(self):
        self.assertFalse(self.diary.is_locked())

        self.diary.create_entry("title", "body")
        self.assertEqual(self.diary.findEntry(1).get_entry_id(), 1)

        self.diary.create_entry("another title", "another_body")
        self.assertEqual(self.diary.findEntry(2).get_entry_id(), 2)

    def test_that_diary_can_delete_entry(self):
        self.assertFalse(self.diary.is_locked())

        self.diary.create_entry("title", "body")
        self.assertEqual(self.diary.findEntry(1).get_entry_id(), 1)

        self.diary.create_entry("another title", "another body")
        self.assertEqual(self.diary.findEntry(2).get_entry_id(), 2)

        self.assertEqual(self.diary.get_number_of_entries(), 2)

        self.diary.delete_entry(1)
        self.assertEqual(self.diary.get_number_of_entries(), 1)

    def test_that_diary_can_update_entries(self):
        self.assertFalse(self.diary.is_locked())

        self.diary.create_entry("title", "body")
        self.assertEqual(self.diary.findEntry(1).get_entry_id(), 1)

        self.diary.update_entry(1, "new title", "new body")
        self.assertEqual(self.diary.findEntry(1).title, "new title")
        self.assertEqual(self.diary.findEntry(1).body, "new body")


if __name__ == '__main__':
    unittest.main()
