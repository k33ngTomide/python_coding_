import unittest

from ClassTasks.create_turple import create_tuple


class MyTestCase(unittest.TestCase):
    def test_that_function_will_return_list_of_tuples(self):
        given1 = [1, 2, 3, 4, 5]
        given2 = [6, 7, 8, 9, 10]

        expected = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
        self.assertEqual(expected, create_tuple(given1, given2))

    def test_that_function_will_return_list_of_tuples_(self):
        given1 = [1, 2, 3, 4, 5, 11]
        given2 = [6, 7, 8, 9, 10]

        expected = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (11, )]
        self.assertEqual(expected, create_tuple(given1, given2))

    def test_that_function_will_return_list_of_tuples_A(self):
        given1 = [1, 2, 3, 4, 5, 11, 12, 13, 14]
        given2 = [6, 7, 8, 9, 10]

        expected = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (11, ), (12, ), (13, ), (14, )]
        self.assertEqual(expected, create_tuple(given1, given2))

    def test_that_function_will_return_list_of_tuples_B(self):
        given2 = [1, 2, 3, 4, 5, 11, 12, 13, 14]
        given1 = [6, 7, 8, 9, 10]

        expected = [(6, 1), (7, 2), (8, 3), (9, 4), (10, 5), (11, ), (12, ), (13, ), (14, )]
        self.assertEqual(expected, create_tuple(given1, given2))

if __name__ == '__main__':
    unittest.main()
