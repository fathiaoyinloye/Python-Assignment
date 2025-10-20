from transaction_app_funtion import *
print(show_menu())
balance = 0
choice = "0"
history_list = []
while(choice != "4"):
	choice = input("Choose your choice: ")
	match choice:
		case "1":
			deposit = float(input("Enter Deposit Amount: "))
			output = deposit(deposit, balance)
			print(output)
		case "2": 
			withdrawal = float(input("Enter Withdrawal Amount: "))
			output = withdraw(withdrawal, balance)
			print(output)

			
		case "3": 
			output = transactions(history_list)
			print(output)
		case "4": 
			print(f"Final Balance {balance}")
			print("Thank you for using Transaction Log Application")
			
		case _ : 
			print("Invalid Input")
			print(show_menu())
