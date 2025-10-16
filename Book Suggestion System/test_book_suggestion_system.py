import unittest
import book_suggestion_system_functions

class TestBookSuggestionSystem(unittest.TestCase):
	def test_suggest_book_existence(self):
		book_suggestion_system_functions.suggest_book(1)
	def test_suggest_book_existence(self):
		book_suggestion_system_functions.suggest_books(1)
	def test_get_menu_existence(self):
		book_suggestion_system_functions.get_menu()