from book_suggestion_system_functions import *
print(get_menu())
choice = 0
while(choice != "6"):
	choice = input("Enter operation: ")
	match choice:
		case "1": 
			other_suggestion = True
			while(other_suggestion ):
				result = suggest_books()
				book = result[0]
				page = result[1]
				output = f"""
				Book for the day:
				Book Title: {book}
				Page: {page} 
				"""
				print(output)
				choice = input("Would you like to get another suggestion?(yes/no): ").lower()
				match choice:
					case "yes":other_suggestion = True
					case "no":
						print(get_menu())
						other_suggestion = False
					case _: print("Invalid Input")

			
		case "2": 
			choice = input("Enter the book title to add: ").upper()
			add_new_book(choice)
			print(get_menu())

		case "3": 
			choice = input("Enter the book title to remove: ").upper()
			remove_book(choice)
			print(get_menu())

		case "4": 
			print("Update Book")
			print(get_menu())
		case "5": 
			name = show_books()
			print(name)
			print(get_menu())
		case "6": print("Exit")
		case _ : print("Invalid Input,Please choose from the above menu")

