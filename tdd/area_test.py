import unittest
from area import area
import math


class TestAreaFunction(unittest.TestCase):

    def test_that_area_is_calculated(self):
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), math.pi * 2 ** 2)


if __name__ == '__main__':
    unittest.main()
