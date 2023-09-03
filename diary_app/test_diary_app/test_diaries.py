import unittest

from diary_app.diaries import Diaries
from diary_app.exceptions_list import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.diaries = Diaries()

    def test_that_diaries_can_add_diary(self):
        self.diaries.add("username", "password")
        self.assertEqual(self.diaries.get_size(), 1)

    def test_that_diaries_can_find_a_diary(self):
        self.diaries.add("username", "password")
        self.diaries.add("username1", "password")
        self.diaries.add("username2", "password")
        self.diaries.add("username3", "password")
        self.diaries.add("username4", "password")
        self.assertEqual(self.diaries.get_size(), 5)

        self.assertEqual(self.diaries.find_by_username("username1").get_username(), "username1")

    def test_that_diaries_can_delete_a_diary(self):
        self.diaries.add("username7", "password")
        self.diaries.add("username1", "password")
        self.diaries.add("username2", "password")
        self.diaries.add("username3", "password")
        self.diaries.add("username4", "password")
        self.assertEqual(self.diaries.get_size(), 5)

        self.diaries.delete("username3", "password")
        self.assertEqual(self.diaries.get_size(), 4)


if __name__ == '__main__':
    unittest.main()
