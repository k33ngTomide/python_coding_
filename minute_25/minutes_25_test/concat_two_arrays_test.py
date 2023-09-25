import unittest

from minute_25 import concat_two_arrays


class MyTestCase(unittest.TestCase):
    def test_that_the_arrays_are_returned_concatenated(self):
        array1 = [1, 2, 3, 4, 5]
        array2 = [6, 7, 8]

        actual = concat_two_arrays.add(array1, array2)
        expected = [5, 4, 3, 2, 1, 8, 7, 6]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
