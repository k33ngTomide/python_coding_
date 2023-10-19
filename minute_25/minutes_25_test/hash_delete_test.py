import unittest

from minute_25 import hash_delete


class MyTestCase(unittest.TestCase):
    def test_hash_delete(self):
        self.assertEqual(True, hash_delete.is_equal_after_backspace("ab#c", "ak#c"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
