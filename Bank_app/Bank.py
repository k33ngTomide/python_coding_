from Account import *


class Bank:
    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.account_list = []

    def register(self, first_name: str, last_name: str, pin: str) -> None:
        full_name = f"{first_name} {last_name}"
        account = Account(self.__generate_account_number(), full_name, pin)
        self.account_list.append(account)

    def __generate_account_number(self) -> str:
        return f'{len(self.account_list) + 1}'

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
        for account in self.account_list:
            if account.account_number == account_number:
                return account


