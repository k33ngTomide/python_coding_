import calendar
import tkinter as tk
from tkinter import simpledialog
from menstrual_app.menstrual_cycle import MenstrualCalculator


class MenstrualApp:
    def __init__(self):
        self.menstrual_calculator = MenstrualCalculator()

    def welcome(self):
        message = """
            Welcome to Menstrual Calculator Application
            Note That:
            +++++ This Application is Made for Women/Ladies With Regular Menstrual Cycle.

            +++++ If Your Cycle Is IRREGULAR, Consult your Doctor.

            +++++ The Output of this application should be used alongside your personal
                  body Symptoms to get the perfect predictions.

            +++++ The output depends on the dates user input, Kindly Input correct Information.

            """
        self.display(message)
        self.start_input()

    def start_input(self):
        user_input = self.input("""
        What Do you want to do?
        1. Know Next Period Date.
        2. Get Ovulation Period.
        3. Get Fertility Period.
        4. Get Safe Period.
        5. Exit.
        
        Enter Your Choice""")
        if user_input == "1":
            self.next_period()
        elif user_input == "2":
            self.ovulation_period()
        elif user_input == "3":
            self.fertility_period()
        elif user_input == "4":
            self.safe_period()
        elif user_input == "5":
            self.exit_application()
        else:
            self.invalid_input()

    def next_period(self):
        date_of_last_period = self.input("""Enter the date your last Period started (Format: yyyy-mm-dd)""")
        try:
            self.validate_date(date_of_last_period)
            cycle_length = int(self.input("Enter your cycle length "))
            flow_days = int(self.input("Enter your flow days"))
            design = "!" * 50
            period_start = self.menstrual_calculator.get_start_date_of_next_period(date_of_last_period, cycle_length,
                                                                                   flow_days)
            period_end = self.menstrual_calculator.get_end_date_of_next_period(
                self.menstrual_calculator.get_start_date_of_next_period(
                    date_of_last_period, cycle_length, flow_days), flow_days)
            message = f"""
            {design}
            Next Period Start:  {period_start}
            Next Period End:  {period_end}
            {design}
            
            {self.print_calendar(period_start)}"""
            self.display(message)
            self.start_input()
        except (ValueError, TypeError):
            self.display()
            self.safe_period()

    @staticmethod
    def validate_date(date_of_last_period):
        day = int(date_of_last_period[8:])
        month = int(date_of_last_period[5:7])

        if not date_of_last_period.startswith("2023"):
            raise ValueError("Invalid date, Remember This is 2023")
        if month > 12:
            raise ValueError("Invalid Month, Month cannot be greater than 12")
        if day > 31:
            raise ValueError("Day is never greater than 31")

    def ovulation_period(self):
        date_of_last_period = self.input("""
            Enter the date your last Period started (Format: yyyy-mm-dd)""")

        try:
            self.validate_date(date_of_last_period)
            cycle_length = int(self.input("Enter your cycle length "))
            flow_days = int(self.input("Enter your flow days"))

            ovulation_date = self.menstrual_calculator.get_ovulation_day(date_of_last_period, cycle_length, flow_days)
            design = "*" * 50
            message = f"""
            {design}
            Ovulation date: {ovulation_date}
            {design}
            
            {self.print_calendar(ovulation_date)}
                """
            self.display(message)
            self.start_input()
        except (ValueError, TypeError):
            self.display("Invalid input or Invalid date format. Please try again.")
            self.ovulation_period()

    def fertility_period(self):
        ovulation_date = self.input("Enter your Ovulation Date (Format: yyyy-mm-dd)")

        try:
            self.validate_date(ovulation_date)
            fertility_start = self.menstrual_calculator.get_start_of_fertility_date(ovulation_date)
            fertility_end = self.menstrual_calculator.get_end_of_fertility_date(ovulation_date)
            design = "*" * 50
            message = f"""
            {design}
            Fertility Period Start:  {fertility_start}
            Fertility Period End:  {fertility_end}
            {design}
            
            {self.print_calendar(fertility_start)}"""
            self.display(message)
            self.start_input()
        except (ValueError, TypeError):
            self.display("Invalid input or invalid date format. Please try again.")
            self.fertility_period()

    def safe_period(self):
        date_of_last_period = self.input("""
            Remember: Abstinence is the the 100% way to be safe.

            Enter the date your last Period started (Format: yyyy-mm-dd)""")
        try:
            self.validate_date(date_of_last_period)
            cycle_length = int(self.input("Enter your cycle length "))
            flow_days = int(self.input("Enter your flow days"))
            design = "!" * 30
            safe_start = self.menstrual_calculator.get_start_of_safe_period(date_of_last_period, flow_days)
            safe_end = self.menstrual_calculator.get_end_of_safe_period(date_of_last_period, cycle_length, flow_days)
            message = f"""
            {design}
            Safe Period Start:  {safe_start}
            Safe Period End:  {safe_end}
            {design}
            
            {self.print_calendar(safe_start)}"""

            self.display(message)
            self.start_input()
        except (ValueError, TypeError):
            self.display("Invalid input or invalid date format. Please try again.")
            self.safe_period()

    def exit_application(self):
        self.display("Stay Safe, Remember to use protection... Bye")
        quit()

    @staticmethod
    def print_calendar(date: str):
        year = int(date[:4])
        month = int(date[5:7])
        cal = calendar.TextCalendar()

        return cal.formatmonth(year, month)

    def invalid_input(self):
        self.display("Invalid Input")
        self.start_input()

    @staticmethod
    def display(message):
        print(message)

        # window = tk.Tk()
        # window.geometry("700x500")
        # window.title("Result")
        #
        # label = tk.Label(window, text=message, font=("Arial", 20))
        # label.grid(row=0, column=0)
        #
        # button = tk.Button(window, text="OK", command=window.destroy)
        # button.grid(row=1, column=1)
        #
        # window.mainloop()

    @staticmethod
    def input(prompt):
        # return tk.simpledialog.askstring("Input", prompt)
        return input(f"{prompt}:  ")


if __name__ == '__main__':
    MenstrualApp().welcome()
