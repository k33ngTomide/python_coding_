import unittest

from bank_issues.bank import Bank


class TestBank(unittest.TestCase):

    def setUp(self) -> None:
        self.bank = Bank("Afunimawobe Bank")
        self.account = self.bank.register("firstName", "lastName", "0000")

    def test_That_Bank_Can_Register_Customer(self):
        self.assertEqual(1, self.bank.get_no_of_customers())

    def test_That_Deposit_MoneyWorks(self):
        self.bank.deposit(15_200, self.account.account_number)
        self.assertEqual(15_200, self.bank.find_account(self.account.account_number).get_balance("0000"))

    def test_That_Withdrawal_MoneyWorks(self):
        self.bank.deposit(15_200, self.account.account_number)
        self.assertEqual(15_200, self.bank.find_account(self.account.account_number).get_balance("0000"))

        self.bank.withdraw(3_000, self.account.account_number, "0000")
        self.assertEqual(12_200, self.bank.find_account(self.account.account_number).get_balance("0000"))

    def test_That_Transfer_MoneyWorks(self):
        account_2 = self.bank.register("firstName1", "lastName1", "1111")
        self.assertEqual(2, self.bank.get_no_of_customers())

        self.bank.deposit(25_500, self.account.account_number)
        self.assertEqual(25_500, self.bank.find_account(self.account.account_number).get_balance("0000"))

        self.assertEqual(0, self.bank.find_account(account_2.account_number).get_balance("1111"))

        self.bank.transfer(10_000, self.account.account_number, account_2.account_number, "0000")

        self.assertEqual(15_500, self.bank.find_account(self.account.account_number).get_balance("0000"))
        self.assertEqual(10_000, self.bank.find_account(account_2.account_number).get_balance("1111"))
