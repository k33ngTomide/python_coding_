import unittest

from employee.employee import Employee
from employee.employee_exceptions import NegativeHoursException


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.employee1 = Employee("Muiliyu Sodiq", "Human Resources")
        self.employee2 = Employee("Akintomide Muiliyu", "Hydrology Department")
        self.employee3 = Employee("Akin Tomide", "Dump Department")
        self.employee4 = Employee("AkinTomide Tomide", "Dump Department")

    def test_that_employee_was_created(self):
        self.assertEqual("Muiliyu Sodiq", self.employee1.get_emp_name())
        self.assertEqual("Human Resources", self.employee1.get_emp_department())

    def test_that_employee_salary_can_be_calculated(self):
        salary = self.employee1.calculate_emp_salary(12)
        self.assertEqual("$120", salary)

    def test_that_employee_calculator_raises_exception_if_hours_worked_is_negative(self):
        self.assertRaises(NegativeHoursException, self.employee1.calculate_emp_salary, -5)

    def test_that_employee_department_can_be_changed(self):
        self.employee1.emp_assign_department("Account Department")
        self.assertEqual("Account Department", self.employee1.get_emp_department())

    def test_that_employee_details_can_be_printed(self):
        self.assertEqual(
            Employee("Muiliyu Sodiq", "Human Resources").print_emp_details(),
            self.employee1.print_emp_details())

    def test_that_employee_id_number_increases(self):
        self.assertEqual(1, self.employee1.get_emp_id())
        self.assertEqual(2, self.employee2.get_emp_id())
        self.assertEqual(3, self.employee3.get_emp_id())
        self.assertEqual(4, self.employee4.get_emp_id())
