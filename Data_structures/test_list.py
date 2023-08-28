import unittest

from Array_list import *


class TestList(unittest.TestCase):
    def test_that_if_i_add_to_list_it_gets_added(self):
        new_list = Array_list(5)
        new_list.append(56)
        self.assertEquals(new_list.get(0), 56)


if __name__ == '__main__':
    unittest.main()
