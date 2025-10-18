from book_suggestion_two_functions import *

books =  ["THE SUBTLE ART OF NOT GIVING A FUCK", "SMILE ITS SUNNAH", "HOW TO KILL A MAN AND GET AWAY WITH IT", "HALF A YELLOW SUN", "THINGS FALL APART", "THERE WAS A COUNTRY", "AMERICANA", "PURPLE HIBISCUS", "OTHELLO","SCARS OF THE PAST", "DREAM IT'S POSSIBLE", "BORN WITHOUT A SILVER SPOON","THE BEAUTIFUL ONES ARE NOT YET BORN", "SECOND CLASS CITIZEN", "PASS ON THE BATON", "THE FLOW", "STAY WITH ME", "OLIVER TWIST"]

print(get_menu())
choice = 0
while(choice != "6"):
	choice = input("Enter operation: ")
	match choice:
		case "1": 
			other_suggestion = True
			while(other_suggestion ):
				result = suggest_book(books)
				book = result[0]
				page = result[1]
				output = f"""
				Book for the day:
				Book Title: {book}
				Page: {page} 
				"""
				print(output)
				choice = input("Would you like to get another suggestion?(yes/no): ").lower()
				while(choice != "yes" and choice != "no"):
					print("Invalid Input")
					choice = input("Would you like to get another suggestion?(yes/no): ").lower()
					if choice == "yes" or choice == "no":
						break
		
				match choice:
					case "yes":other_suggestion = True
					case "no":
						print(get_menu())
						other_suggestion = False
			
		case "2": 
			choice = input("Enter the book title to add: ").upper()
			result = add_new_book(books,choice)
			print(result)
			print(get_menu())

		case "3": 
			choice = input("Enter the book title to remove: ").upper()
			result = remove_book(books, choice)
			print(result)
			print(get_menu())

		case "4": 
			old_book = input("Enter the old book title: ").upper()
			new_book = input("Enter the new book title: ").upper()
			result = update_book(books, old_book, new_book)
			print(result)
			print(get_menu())
		case "5": 
			name = show_books(books)
			print(name)
			print(get_menu())
		case "6": print("Exit")
		case _ : print("Invalid Input,Please choose from the above menu")

