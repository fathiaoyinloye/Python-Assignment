import unittest
from multifuel_dispenser_app import *

class TestMultiDispenserApp(unittest.TestCase):
	def test_that_calculate_liter_function_exist(self):
		calculate_liter("1", 5000)

	def test_that_calculate_liter_function_calculates_liters_for_kerosene(self):
		actual = calculate_liter("1", 5000)
		expected = 5.0
		self.assertEqual(actual,expected)

	def test_that_calculate_liter_function_does_not_calculates_amount_less_than_a_liter_for_kerosene(self):
		actual = calculate_liter("1", 100)
		expected = "Amount must be greater than a litre's price"
		self.assertEqual(actual,expected)



	def test_that_calculate_liter_function_calculates_liters_for_disel(self):
		actual = calculate_liter("2", 5000)
		expected = 10
		self.assertEqual(actual,expected)

	def test_that_calculate_liter_function_calculates_liters_for_gas(self):
		actual = calculate_liter("3", 9000)
		expected = 6
		self.assertEqual(actual,expected)

	def test_that_calculate_liter_function_calculates_liters_for_petrol(self):
		actual = calculate_liter("4", 1400)
		expected = 2
		self.assertEqual(actual,expected)

	def test_that_calculate_cost_function_exist(self):
		calculate_cost("1", 10)

	def test_that_calculate_liter_function_calculates_cost_for_kerosene(self):
		actual = calculate_cost("1", 2)
		expected = 2000
		self.assertEqual(actual,expected)

	def test_that_calculate_cost_function_does_not_calculates_amount_less_than_1_or_greater_than_50_for_kerosene(self):
		actual = calculate_cost("2", -4)
		expected = "Liters must be between 1 - 50"
		self.assertEqual(actual,expected)



	def test_that_calculate_cost_function_calculates_cost_for_disel(self):
		actual = calculate_cost("2", 6)
		expected = 3000
		self.assertEqual(actual,expected)

	def test_that_calculate_cost_function_calculates_cost_for_gas(self):
		actual = calculate_cost("3", 2)
		expected = 3000
		self.assertEqual(actual,expected)

	def test_that_calculate_cost_function_calculates_cost_for_petrol(self):
		actual = calculate_cost("4", 4)
		expected = 2800
		self.assertEqual(actual,expected)

	def test_that_show_receipt_function_exist(self):
		show_receipts()

	def test_that_show_transactions_function_exist(self):
		show_transactions()




	