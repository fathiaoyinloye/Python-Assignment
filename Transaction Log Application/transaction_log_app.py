from transaction_functions import *
print(show_menu())
account_balance = 0
transaction = " "
choice = "0"
while(choice != "4"):
	choice = input("Choose your choice: ")
	match choice:
		case "1":
			deposit = int(input("Enter Deposit Amount: "))
			account_balance += deposit
			print(get_deposit(deposit, account_balance))
		case "2": 
			withdrawal = int(input("Enter Withdrawal Amount: "))
			print(withdraw(withdrawal, account_balance))
			account_balance = account_balance - withdrawal




		case "3": print("Show transactions")
		case "4": print("Bye!")
		case _ : 
			print("Invalid Input")
			print(show_menu())
