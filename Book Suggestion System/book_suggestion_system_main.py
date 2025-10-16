from book_suggestion_system_functions import *
print(get_menu())
choice = 0
while(choice != "6"):
	choice = input("Enter operation: ")
	match choice:
		case "1": print("Get Suggestions")
		case "2": print("Add Book")
		case "3": print("Remove Book")
		case "4": print("Update Book")
		case "5": print("Show Books")
		case "6": print("Exit")
		case _ : print("Invalid Input,Please choose from the above menu")

