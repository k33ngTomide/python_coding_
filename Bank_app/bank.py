import random

from Bank_app.exceptions import *
from account import Account


class Bank:
    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__account_list = []
        self.__list_of_account_number = []

    def register(self, first_name: str, last_name: str, pin: str):
        full_name = f"{first_name} {last_name}"
        account = Account(self.__generate_account_number(), full_name, pin)
        self.__account_list.append(account)
        return account.get_account()

    def __generate_account_number(self) -> str:
        account_number = f"71{random.randint(10000000, 99000000)}"
        self.__validate_account_number(account_number)
        return account_number

    def __validate_account_number(self, account_number):
        if account_number not in self.__list_of_account_number:
            self.__list_of_account_number.append(account_number)
        else:
            self.__generate_account_number()

    def deposit(self, amount, account_number):
        found_account = self.find_account(account_number)
        found_account.deposit(amount)

    def withdraw(self, amount, account_number, pin):
        found_account = self.find_account(account_number)
        found_account.withdraw(amount, pin)

    def transfer(self, amount, sender_account, receiver_account, pin):
        sending_account = self.find_account(sender_account)
        sending_account.withdraw(amount, pin)

        receiving_account = self.find_account(receiver_account)
        receiving_account.deposit(amount)

    def check_balance(self, account_number, pin):
        found_account = self.find_account(account_number)
        return found_account.check_balance(pin)

    def find_account(self, account_number) -> Account:
        for account in self.__account_list:
            if account.account_number == account_number:
                return account
        raise AccountNotFoundException("Account Not Found")

    def get_no_of_customers(self):
        return len(self.__account_list)
