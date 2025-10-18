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

def suggest_book(books):
	
	random.shuffle(books)
	random_book = random.choice(books)
	random_pages = random.randrange(1,101)
	return random_book, random_pages
	
	
def add_new_book(books,book):
	books.append(book)

	return "Book added successfully"

def remove_book(books, book):
	if book in books:
		books.remove(book)
		return "Book successfully removed"
	else:
		return "Book entered not in your list of books"
def remove_book(books, book):
	if book in books:
		books.remove(book)
		return "Book successfully removed"
	else:
		return "Book entered not in your list of books"
def update_book(books, old_title, new_title):
	if old_title in books:
		books.remove(old_title)
		books.append(new_title)
		return "Book successfully updated"

	else:
		return "Book to be updated not in the library"
		 
def show_books(books):
	count = 1
	for book in books:
		print(f"{count}\t{book}")
		count += 1
	return "These are all the books available for you"

