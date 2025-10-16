import unittest
import transaction_log_app_function

class TestTransactionLogApp(unittest.Testcase):
	def test_the_existence_of_function(self):
		transaction_log_app_function.get_deposit(34)