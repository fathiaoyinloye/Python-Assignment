import unittest
import transaction_log_app_two_function

class TestTransactionLogApp(unittest.TestCase):
	def test_existence_of_transaction_app(self):
		transaction_log_app_two_function.deposit(1,0,0)

	def test_if_deposit_function_sums_up_deposited_money(self):
		actual= transaction_log_app_two_function.deposit(1000,0 ,0)
		expected = 1000
		self.assertEqual(actual,expected)