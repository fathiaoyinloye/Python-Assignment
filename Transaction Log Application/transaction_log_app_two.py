from transaction_functions import *
print(show_menu())
account_balance = 0
transaction = " "
choice = input("Choose your choice: ")
match choice:
	case "1":
		deposit = int(input("Enter Deposit Amount: "))
		account_balance += deposit
		print(get_deposit(deposit, account_balance))
	case "2": 
		withdrawal = int(input("Enter Deposit Amount: "))
		if account_balance < withdrawal:
			account_balance -= 0

		else:
			account_balance -= withdrawal
		print(withdraw(withdrawal, account_balance))



	case "3": print("Show transactions")
	case "0": print("Bye!")
	case _ : 
		print("Invalid Input")
		print(show_menu())
