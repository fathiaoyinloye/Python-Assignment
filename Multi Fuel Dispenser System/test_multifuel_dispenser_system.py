import unittest
import multifuel_dispenser_system_function

class TestMultifuelDispenserSystem(unittest.TestCase):
	def test_calculate_total_cost_function_existence(self):
		multifuel_dispenser_system_function.calculate_total_cost("diesel",3,498)

	def test_calculate_total_cost_function_calculate_total_cost(self):
		actual = multifuel_dispenser_system_function.calculate_total_cost("kerosene", 5,1000)
		expected = 5000
		self.assertEqual(actual,expected)

	def test_calculate_total_cost_function_rejects_input_less_than_one_and_greater_than_fifty(self):
		actual = multifuel_dispenser_system_function.calculate_total_cost("diesel", -1,1000)
		expected = "Liters must be between 1 - 50"
		self.assertEqual(actual,expected)

	def test_calculate_liters_existence(self):
		multifuel_dispenser_system_function.calculate_total_cost("diesel",3,498)


	def test_calculate_total_cost_function_rejects_input_less_than_the_price(self):
		actual = multifuel_dispenser_system_function.calculate_liters("diesel", 300,1000)
		expected = "Amount must be above a liter price"
		self.assertEqual(actual,expected)

	def test_show_transactions_existence(self):
		transaction = ["boy", "girl", "sister"]
		multifuel_dispenser_system_function.show_transactions(transaction)

	def test_show_transactions_does_not_show_an_empty_transaction_list(self):
		transaction = []
		actual = multifuel_dispenser_system_function.show_transactions(transaction)
		expected = actual == "No transaction made yet"
		self.assertTrue =(expected)
		


	