import unittest

from ClassTasks import kiss_dry


class MyTestCase(unittest.TestCase):
    def test_that_new_word_will_be_returned_according_to_the_indices_given(self):
        indices = [6, 2, 3, 4, 1, 0, 5]
        actual = kiss_dry.get_word("kissdry", indices)

        self.assertEqual("yssdikr", actual)


if __name__ == '__main__':
    unittest.main()
