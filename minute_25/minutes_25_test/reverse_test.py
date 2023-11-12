import unittest

from minute_25 import reversal


class MyTestCase(unittest.TestCase):
    def test_that_each_word_got_reversed(self):
        given = "A better place"
        expected = "A retteb ecalp"
        self.assertEqual(expected, reversal.reverse_each(given))

    def test_that_each_word_got_reversed_(self):
        given = "Switch off Moyin's phone"
        expected = "hctiwS ffo s'niyoM enohp"
        self.assertEqual(expected, reversal.reverse_each(given))


if __name__ == '__main__':
    unittest.main()
