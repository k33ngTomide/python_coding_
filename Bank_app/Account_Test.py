import unittest
from Account import *


class TestAccount(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.account = None

    def setUp(self) -> None:
        self.account = Account("1", "Muiliyu Sodiq", "1234")

    def test_that_account_can_Deposit_Money_And_Increase_Balance(self):
        self.account.deposit(3000)
        self.assertEqual(3000, self.account.check_balance("1234"))

    def test_that_checking_balance_with_wrong_pinThrowsException(self):
        self.account.deposit(10_000)
        self.assertRaises(ValueError, self.account.check_balance, "0010")

    def test_that_money_can_be_withdrawn_from_the_account(self):
        self.account.deposit(5_000)
        self.assertEqual(5_000, self.account.check_balance("1234"))

        self.account.withdraw(2_000, "1234")
        self.assertEqual(3_000, self.account.check_balance("1234"))

    def testThatWithdrawalWithWrongPinRaisesExceptionAndBalanceIsUntouched(self):
        self.account.deposit(10_000)
        self.assertRaises(ValueError, self.account.withdraw, 2000, "0121")
        self.assertEqual(10_000, self.account.check_balance("1234"))

    def testThatWithdrawalWithWrongAmountRaisesExceptionAndBalanceIsUntouched(self):
        self.account.deposit(10_000)
        self.assertRaises(ValueError, self.account.withdraw, -2000, "1234")
        self.assertEqual(10_000, self.account.check_balance("1234"))

    def testThatWithdrawalAmountMoreThanBalanceRaisesExceptionAndBalanceIsUntouched(self):
        self.account.deposit(5_000)
        self.assertRaises(ValueError, self.account.withdraw, 18000, "1234")
        self.assertEqual(5_000, self.account.check_balance("1234"))

    def testThatPinCanBeChanged_ByTryingToWithdrawWithNewPin(self):
        self.account.deposit(5_800)
        self.account.update_pin("1234", "1111")
        self.assertEqual(5_800, self.account.check_balance("1111"))

    def testThatWithdrawalWithOldPinThrowsAnException(self):
        self.account.deposit(1_300)
        self.account.update_pin("1234", "1111")
        self.assertRaises(ValueError, self.account.check_balance, "1234")
