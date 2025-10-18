import random

def get_menu():
	menu = """
*********************************************************
*	Welcome To The Book Suggestion System		*
*********************************************************
*    Click any of the following to perform operation 	*
*		1 	Get Suggestions			*
*		2	Add Book			*
*		3	Remove Book			*
*		4	Update Book			*
*		5	Show All Books			*
*		6	Exit System			*
*********************************************************
	"""
	return menu
books = ["the subtle art of not giving a fuck", "smile its Sunnah", "How to kill a man and get away with it", "Half a yellow sun", "Things fall apart", "There was a country", "Americana", "Purple Hibiscus", "Othello","Scars of the past", "Dream it's possible", "Perspire to Acquire The Desire", "The Flow", "Stay with me", "Oliver Twist"]
wanted_books = []

def suggest_books():
	
	random.shuffle(books)
	random_books = random.choice(books)
	wanted_books.append(random_books)
	random_pages = random.randrange(1,101)
	return random_books, random_pages
	
	
	
def add_new_book(book):
	if type(book) == int:
		return "Invalid Input"
	else:
		wanted_books.append(book)
		return "Book added successfully"
def remove_book(book):
	for element in wanted_books:
		if book != element:
			return "Book entered not in your list of books"
		else:	
			wanted_books.remove(book)
			return "Book successfully removed"
def show_books():
	if wanted_books == []:
			return "No book added"
	else:	
		for book in wanted_books:
			return wanted_books
