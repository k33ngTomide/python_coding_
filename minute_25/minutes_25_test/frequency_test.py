import unittest

from minute_25 import frequency


class MyTestCase(unittest.TestCase):
    def test_that_(self):
        given = [3, 2, 3]

        self.assertEqual(3, frequency.get_most_frequent(given))


if __name__ == '__main__':
    unittest.main()
