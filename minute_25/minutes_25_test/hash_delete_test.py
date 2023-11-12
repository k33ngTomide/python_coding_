import unittest

from minute_25 import hash_delete


class MyTestCase(unittest.TestCase):
    def test_hash_delete(self):
        self.assertEqual(True, hash_delete.is_equal_after_backspace("a#b#d#pqrs#", "ac#d##pqr"))

    def test_that_all_characters_are_replaced(self):
        given = "The&name&of&my&guy&is&Seyi%And&he&is&a&mad&guy"
        expected = "The name of my guy is Seyi.    And he is a mad guy"
        self.assertEqual(expected, hash_delete.impl_space_and_tab(given))


if __name__ == '__main__':
    unittest.main()
