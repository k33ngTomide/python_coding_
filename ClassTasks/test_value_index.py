import unittest

from ClassTasks.value_index import sum_list


class MyTestCase(unittest.TestCase):
    def test_that_the_indices_that_sum_up_to_given_value_is_returned(self):
        given = [5, 4, 9, 7, 2, 0]
        expected = [2, 3]

        self.assertEqual(expected, sum_list(given, 16))

    def test_that_the_indices_that_sum_up_to_given_value_is_returned_(self):
        given = [2, 5, 8, 4, 1, 0]
        expected = [0, 4]

        self.assertEqual(expected, sum_list(given, 3))


if __name__ == '__main__':
    unittest.main()
