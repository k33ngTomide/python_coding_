from employee.employee_exceptions import NegativeHoursException


class Employee:
    __emp_id = 0

    def __init__(self, emp_name: str, emp_department: str):
        self.__emp_name = emp_name
        self.__emp_department = emp_department
        self.__hourly_rate = 10
        self.__emp_id += 1

    def get_emp_id(self):
        return self.__emp_id

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_department(self):
        return self.__emp_department

    def calculate_emp_salary(self, number_of_hours_worked) -> str:
        if number_of_hours_worked < 0:
            raise NegativeHoursException("Number of Hours Worked must be positive")
        return f"${str(self.__hourly_rate * number_of_hours_worked)}"

    def emp_assign_department(self, department):
        self.__emp_department = department

    def print_emp_details(self):
        design = "-" * 20
        return (f'{design} \nEmployee Name: {self.get_emp_name()}'
                f'\nEmployee Id: {self.get_emp_id()}'
                f'\nEmployee department: {self.get_emp_department()} \n{design}')
