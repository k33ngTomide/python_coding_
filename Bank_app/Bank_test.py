from Bank import *
import unittest


class BankTest(unittest.TestCase):

    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.bank = None

    def setUp(self) -> None:
        self.bank = Bank("Semicolon Bank")
        self.bank.register("firstName", "lastName", "0000")

    def test_That_Bank_Can_Register_Customer(self):
        self.assertEqual(Account("1", "firstName lastName", "0000").get_account(),
                         self.bank.find_account("1").get_account())

    def test_That_Deposit_MoneyWorks(self):
        self.bank.deposit(15_200, "1")
        self.assertEqual(15_200, self.bank.check_balance("1", "0000"))

    def test_That_Withdrawal_MoneyWorks(self):
        self.bank.deposit(15_200, "1")
        self.assertEqual(15_200, self.bank.check_balance("1", "0000"))

        self.bank.withdraw(3_000, "1", "0000")
        self.assertEqual(12_200, self.bank.check_balance("1", "0000"))

    def test_That_Transfer_MoneyWorks(self):
        self.bank.register("firstName1", "lastName1", "1111")
        self.bank.deposit(25_500, "1")
        self.assertEqual(25_500, self.bank.check_balance("1", "0000"))

        self.assertEqual(0, self.bank.check_balance("2", "1111"))

        self.bank.transfer(10_000, "1", "2", "0000")

        self.assertEqual(15_500, self.bank.check_balance("1", "0000"))
        self.assertEqual(10_000, self.bank.check_balance("2", "1111"))
