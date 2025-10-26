import unittest
from code_leveling_functions import *
class TestCodeLevelingFunctions(unittest.TestCase):
	def test_that_append_to_tuple_is_returning_a_tuple(self):
		numbers = ([1,2,4],[7,9,7])
		actual= type(append_to_tuple(numbers, 7))
		expected = tuple
		self.assertEqual(actual,expected)

	def test_that_append_to_tuple_is_appending_a_new_number(self):
		numbers = ([1,2,4],[7,9,7])
		actual= append_to_tuple(numbers, 7)
		expected = ([1,2,4,7],[7,9,7])
		self.assertEqual(actual,expected)

	def test_that_change_element_changes_the_inner_list(self):
		numbers = (1,2,[3,4],5)
		result= change_element(numbers)
		actual = result[2]
		expected = [3,99]
		self.assertEqual(actual,expected)

	def test_that_covert_tuple_to_list_to_tuple_append_another_element_to_the_tuple(self):
		my_tuple =  ("apple","banana")
		actual = covert_tuple_to_list_to_tuple(my_tuple)
		expected = ("apple","banana", "mango")
		self.assertEqual(actual,expected)
	
	def test_that_function_unpack_tuple_unpacks_tuple_passed_to_it(self):
		my_tuple =  (10,20,30)
		actual = unpack_tuple(my_tuple)
		expected = (10,20,30)
		self.assertEqual(actual,expected)

	def test_that_is_even_returns_even_number(self):
		actual = is_even(6)
		expected = True
		self.assertEqual(actual,expected)

	def test_that_even_from_one_to_twenty_return_even_number_of_that_range(self):
		actual = even_from_one_to_twenty()
		expected = [2,4,6,8,10,12,14,16,18,20]
		self.assertEqual(actual,expected)

	def test_that_five_characters_return_word_more_than_five_letters(self):
		actual = five_characters("girlhj")
		expected = "girlhj"
		self.assertEqual(actual,expected)


	def test_that_you_can_extract_word_with_more_than_five_characters(self):
		words = ["boy", "female", "ladies", "lhj", "fghj","hgj"]
		actual = extract_word_with_more_than_five_characters(words)
		expected = ["female", "ladies"]
		self.assertEqual(actual,expected)

	def test_that_function_value_greater_than_two_only_returns_if_the_first_element_is_greater_than_two(self):
		my_tuple = (1, 'S')
		actual = value_greater_than_two(my_tuple)
		expected = None
		self.assertEqual(actual,expected)

	def test_that_function_value_greater_than_two_only_returns_tuples_if_the_first_element_is_greater_than_two(self):
		my_tuple = [(1, 'S'),(2, 'S'),(5, 'S')]
		actual = values_greater_than_two(my_tuple)
		expected = [(5, "S")]
		self.assertEqual(actual,expected)

	def test_that_function_is_divisible_by_three_and_five_returns_number_that_can_be_divided_by_three_and_five(self):
		actual = is_divisible_by_three_and_five(15)
		expected = 15
		self.assertEqual(actual,expected)

	def test_that_function_they_are_divisible_by_three_and_five_returns_numbers_that_can_be_divided_by_three_and_five(self):
		actual = they_are_divisible_by_three_and_five()
		expected = [15,30,45]
		self.assertEqual(actual,expected)

	
	def test_that_function_is_not_palindrome_returns_word_that_are_not_palindrome(self):
		actual = is_not_palindrome("man")
		expected = "man"
		self.assertEqual(actual,expected)

	def test_that_function_they_are_not_palindrome_returns_words_that_are_not_palindrome(self):
		my_list = ["world", "girl", "madam", "chief", "later"]
		actual = they_are_not_palindrome(my_list)
		expected = ["world", "girl", "chief", "later"]
		self.assertEqual(actual,expected)
	

	def test_that_function_convert_to_upper_case_converts_words_to_uppercase(self):
		actual = convert_to_upper_case("man")
		expected = "MAN"
		self.assertEqual(actual,expected)


	def test_that_function_convert_strings_to_uppercase_converts_words_to_uppercase(self):
		my_list = ["world", "girl", "ma__am"]
		actual = convert_strings_to_uppercase(my_list)
		expected =["WORLD", "GIRL", "MA__AM"]
		self.assertEqual(actual,expected)


