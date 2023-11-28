import unittest

from minute_25 import reverse_vowels


class MyTestCase(unittest.TestCase):
    def test_reverse_vowels(self):
        user_input = 'HEllO'
        expected = 'Holle'

        output = reverse_vowels.reverse_vowels(user_input)
        self.assertEqual(output, expected)

    def test_reverse_vowels_again(self):
        user_input = 'Leetcode'
        expected = 'Leotcede'

        output = reverse_vowels.reverse_vowels(user_input)
        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
