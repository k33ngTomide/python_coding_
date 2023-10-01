import unittest

from menstrual_app.menstrual_cycle import MenstrualCalculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.menstrual_calculator = MenstrualCalculator()

    def test_user_can_get_ovulation_period(self):
        ovulation_date = self.menstrual_calculator.get_ovulation_day("2023-09-12", 28, 6)
        self.assertEqual("2023-09-29", ovulation_date)

    def test_user_can_get_fertility_period(self):
        start_of_fertility_date = self.menstrual_calculator.get_start_of_fertility_date("2023-09-29")
        self.assertEqual("2023-09-27", start_of_fertility_date)

        end_of_fertility_date = self.menstrual_calculator.get_end_of_fertility_date("2023-09-29")
        self.assertEqual("2023-10-01", end_of_fertility_date)

    def test_user_can_get_predicted_dates_of_next_period(self):
        start_date_of_next_period = self.menstrual_calculator.get_start_date_of_next_period("2023-09-12", 28, 6)
        self.assertEqual("2023-10-16", start_date_of_next_period)

        end_date_of_next_period = self.menstrual_calculator.get_end_date_of_next_period(start_date_of_next_period, 6)
        self.assertEqual("2023-10-22", end_date_of_next_period)

    def test_user_can_get_safe_period(self):
        start_date_safe_period = self.menstrual_calculator.get_start_of_safe_period("2023-09-12", 6)
        self.assertEqual("2023-09-19", start_date_safe_period)

        end_date_safe_period = self.menstrual_calculator.get_end_of_safe_period("2023-09-12", 28, 6)
        self.assertEqual("2023-09-26", end_date_safe_period)


if __name__ == '__main__':
    unittest.main()
