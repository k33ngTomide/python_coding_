import re
from bank import *


def validate_name(name):
    if re.fullmatch("^[A-Z]+[a-z]*$", name): return
    raise ValueError("Invalid name")


def validate_pin(pin):
    if re.fullmatch("\\d{4}", pin): return
    raise ValueError("Invalid Pin")


class ATM:
    def __init__(self):
        self.bank = Bank("Afunimawobe Bank")

    def main(self):
        self.welcome_menu()

    def welcome_menu(self):
        print("""
        Welcome To Afunimawobe Bank
        press:
        1.  Register Account
        2.  Transact
        3.  Exit Application
        """)

        user_input = input("Enter: ")
        if user_input == "1":
            self.register_account()
        elif user_input == "2":
            self.main_menu()
        elif user_input == "3":
            self.__exit()

    def register_account(self):
        try:
            user_first_name = input("Enter your first name: ")
            validate_name(user_first_name)

            user_last_name = input("Enter your last name: ")
            validate_name(user_last_name)

            user_pin = input("Enter your pin: ")
            validate_pin(user_pin)

            print(self.bank.register(user_first_name, user_last_name, user_pin))
            print("Account Registration Successful")
            self.welcome_menu()

        except ValueError as VError:
            print(VError)
            self.register_account()

    def main_menu(self):
        user_input = input("""
        Welcome 
        Enter:
        1. Deposit
        2. Withdraw
        3. Balance Enquiry
        4. Transfer
        5. Change Pin
        6. Cancel
        
        Enter: """)
        match user_input:
            case "1":
                self.__deposit()
            case "2":
                self.__withdraw()
            case "3":
                self.__balance_enquiry()
            case "4":
                self.__transfer()
            case "5":
                self.__change_pin()
            case "6":
                print("Transaction cancelled")
                self.__another_transaction()
            case _:
                print("Invalid Input")
                self.main_menu()

    def __exit(self):
        print("Thank you for Banking with The Afunimawobe Bank")
        exit(1)

    def __deposit(self):
        try:
            amount = float(input("Enter your amount: "))
            account_number = input("Enter account number: ")
            self.bank.deposit(amount, account_number)
            print("Transaction Successful...")
            self.__another_transaction()

        except NegativeAmountException or AccountNotFoundException as all_error:
            print(all_error)
            self.__another_transaction()

    def __withdraw(self):
        try:
            amount = float(input("Enter your amount: "))
            account_number = input("Enter account number: ")
            pin = input("Enter pin: ")
            self.bank.withdraw(amount, account_number, pin)
            print("Transaction Successful...")

            print(self.bank.check_balance(account_number, pin))

            self.__another_transaction()

        except (NegativeAmountException or InsufficientFundException
                or AccountNotFoundException) as all_error:
            print(all_error)
            self.__another_transaction()

    def __balance_enquiry(self):

        try:
            account_number = input("Enter account number: ")
            pin = input("Enter pin: ")
            print(self.bank.check_balance(account_number, pin))
            self.__another_transaction()

        except WrongPinException or AccountNotFoundException or KeyboardInterrupt as all_error:
            print(all_error)
            self.__another_transaction()

    def __transfer(self):
        try:
            amount = float(input("Enter your amount: "))
            sender_account_number = input("Enter your account number: ")
            receiver_account = input("Enter receiver's account number: ")
            pin = input("Enter pin: ")
            self.bank.transfer(amount, sender_account_number, receiver_account, pin)
            print(self.bank.check_balance(sender_account_number, pin))
            self.__another_transaction()
        except ValueError or WrongPinException or NegativeAmountException as all_error:
            print(all_error)
            self.__another_transaction()

    def __change_pin(self):

        try:
            account_number = input("Enter your account number: ")
            old_pin = input("Enter current pin: ")
            new_pin = input("Enter new pin: ")

            self.bank.find_account(account_number).update_pin(old_pin, new_pin)
            print("Pin Changed Successfully")
            self.__another_transaction()

        except ValueError or WrongPinException as VError:
            print(VError)
            self.__another_transaction()

    def __another_transaction(self):
        user_input = input("""
                    1. Another Transaction
                    2. Main Menu
                    3. Exit Application
                        
                    Enter: """)

        match user_input:
            case "1":
                self.main_menu()
            case "2":
                self.welcome_menu()
            case "3":
                self.__exit()
            case _:
                self.__another_transaction()


if __name__ == '__main__':
    atm = ATM()
    atm.main()
