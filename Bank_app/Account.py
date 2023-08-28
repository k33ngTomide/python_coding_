class Account:

    def __init__(self, account_number: str, account_name: str, pin: str):
        self.__account_number = account_number
        self.__account_name = account_name
        self.__pin = pin
        self.__balance = 0

    def validate_pin(self, pin: str):
        if self.__pin != pin: raise ValueError("Incorrect Pin")

    def validate_amount(self, amount: float):
        if amount < 0: raise ValueError('Amount Cannot Be Negative')

    def deposit(self, amount: float) -> None:
        self.validate_amount(amount)
        self.__balance = self.__balance + amount

    def withdraw(self, amount, pin) -> None:
        self.validate_amount(amount)
        self.validate_pin(pin)
        if amount > self.__balance: raise ValueError('Insufficient Fund')
        self.__balance = self.__balance - amount

    def check_balance(self, pin: str) -> float:
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
        return f"The account name is: {self.account_name}" \
               f"\nThe account Number is: {self.account_number}" \
               f"\nThe Pin of this account is: {int(self.__pin) // 100}**"



