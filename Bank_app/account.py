from Bank_app.exceptions import *


class Account:

    def __init__(self, account_number: str, account_name: str, pin: str):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__pin = pin
        self.__balance = 0.0

    def validate_pin(self, pin: str):
        if self.__pin != pin: raise WrongPinException("Incorrect Pin")

    @staticmethod
    def validate_amount(amount: float):
        if amount < 0: raise NegativeAmountException('Amount Cannot Be Negative')

    def deposit(self, amount: float) -> None:
        self.validate_amount(amount)
        self.__balance = self.__balance + amount

    def withdraw(self, amount, pin) -> None:
        self.validate_amount(amount)
        self.validate_pin(pin)
        if amount > self.__balance: raise InsufficientFundException('Insufficient Fund')
        self.__balance = self.__balance - amount

    def check_balance(self, pin: str) -> str:
        self.validate_pin(pin)
        return self.get_account()

    def get_balance(self, pin:str) -> float:
        self.validate_pin(pin)
        return self.__balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_num: str):
        self.__account_number = account_num

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, account_fullname: str):
        self.__account_name = account_fullname

    def update_pin(self, old_pin, new_pin) -> None:
        self.validate_pin(old_pin)
        self.__pin = new_pin

    def get_account(self) -> str:
        design = "*" * 40
        return (f"{design}"
                f"\nAccount name: {self.account_name}"
                f"\nAccount Number: {self.account_number}"
                f"\nAccount Balance: {self.__balance}"
                f"\n{design}")
