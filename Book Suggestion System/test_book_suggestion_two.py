import unittest
import book_suggestion_two_functions
class TestBookSuggestionSystemm (unittest.TestCase):
	def test_that_function_add_new_book_exist(self):
		book = "I am me"
		books = ["Apollo", "A man call GOD", "Success is a must"]
		book_suggestion_two_functions.add_new_book(books,book)

	def test_that_function_suggest_book_exist(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		book_suggestion_two_functions.suggest_book(books)

	def test_that_function_suggest_book_generate_random_book(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		result = book_suggestion_two_functions.suggest_book(books)
		actual = result[0]
		expected = "Apollo" or "A man call GOD" or "Success is a must"  
		self.assertTrue(expected)

	def test_that_function_suggest_book_generate_random_number_between_one_to_hundred(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		result = book_suggestion_two_functions.suggest_book(books)
		actual = result[1]
		expected = actual  > 0 and actual < 101
		self.assertTrue(expected)

	def test_that_function_suggest_book_generate_random_book_not_sequentially(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		result = book_suggestion_two_functions.suggest_book(books)
		first_result = result[0]
		result = book_suggestion_two_functions.suggest_book(books)
		second_result = result[0]
		expected = first_result != second_result
		self.assertTrue(expected)


	def test_if_add_book_function_add_new_book_to_list(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		book = "I am me"
		actual = book_suggestion_two_functions.add_new_book(books,book)
		result = "Book added successfully"
		self.assertEqual(actual,result)




	def test_if_add_book_function_does_not_add_in_numbers(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		result = book_suggestion_two_functions.add_new_book(books,123)
		result != books.append(123)
		self.assertTrue(result)
		print(result)

	def test_if_remove_book_function_does_accept_remove_book_not_existing_in_the_list_of_added_book(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		book = "Gifted hand"
		actual  = book_suggestion_two_functions.remove_book(books, book)
		expected = "Book entered not in your list of books"
		self.assertEqual(actual,expected)

	def test_if_remove_book_function__remove_book_existing_in_the_list_of_added_book(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		book = "Apollo"
		actual  = book_suggestion_two_functions.remove_book(books, book)
		expected = "Book successfully removed"
		self.assertEqual(actual,expected)

	def test_if_remove_book_function__remove_book_existing_in_the_list_of_added_book_regardless_of_cases(self):
		books = ["APOLLO", "A man call GOD", "Success is a must"]
		book = "Apollo"
		book.upper()
		actual  = book_suggestion_two_functions.remove_book(books, book)
		expected = "Book successfully removed"
		self.assertEqual(actual,expected)



	def test_if_update_book_function__update_book_existing_in_the_list_book(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		old_book = "Apollo"
		new_book = "The gods are not to be blame"
		actual  = book_suggestion_two_functions.update_book(books, old_book, new_book)
		expected = "Book successfully updated"
		self.assertEqual(actual,expected)

	def test_if_update_book_function__does_not_update_book_not_in_the_list__book(self):
		books = ["Apollo", "A man call GOD", "Success is a must"]
		old_book = "Apo"
		new_book = "The gods are not to be blame"
		actual  = book_suggestion_two_functions.update_book(books, old_book, new_book)
		expected = "Book to be updated not in the library"
		self.assertEqual(actual,expected)


		