import unittest
import transaction_app_function
class TestTractionApp(unittest.TestCase):
	def test_deposit_function_existence(self):
		transaction_app_function.deposit(1,2)

	def test_if_deposit_function_adds_money_up(self):
		actual = transaction_app_function.deposit(3000,0)
		expected = 3000
		self.assertEqual(actual, expected)
		
	def test_if_deposit_function_does_not_add_up_negative_value_money_up(self):
		actual = transaction_app_function.deposit(-4000,3000)
		expected = 3000
		self.assertEqual(actual, expected)

	def test_withdraw_function_existence(self):
		transaction_app_function.withdraw(1,2)

	def test_if_withdraw_function_deduct_amount_from_balance(self):
		actual = transaction_app_function.withdraw(1000,3000)
		expected = 2000
		self.assertEqual(actual, expected)

		
	def test_if_withdraw_function_does_not_deduct_amount_greater_than_balance(self):
		actual = transaction_app_function.withdraw(10000,3000)
		expected = 3000
		self.assertEqual(actual, expected)

	def test_transactions_function_existence(self):
		transactions = ["yes", "no", "bye"]
		transaction_app_function.show_transactions(transactions)