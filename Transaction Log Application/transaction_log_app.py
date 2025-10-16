from funtion2 import *
print(show_menu())
balance = 0
history = ""
choice = "0"
history_list = []
while(choice != "4"):
	choice = input("Choose your choice: ")
	match choice:
		case "1":
			deposit = float(input("Enter Deposit Amount: "))
			output = get_deposit(deposit, balance, history)
			balance = output[0]
			history = output[1]
			history_list.append(history)
			print(history)
		case "2": 
			withdrawal = float(input("Enter Withdrawal Amount: "))
			output = withdraw(withdrawal, balance,history)
			balance = output[0]
			history = output[1]
			history_list.append(history)

			print(history)

			

		case "3": 
			output = get_transaction(history_list)
			print(output)
		case "4": 
			print(f"Final Balance {balance}")
			print("Thank you for using Transaction Log Application")
			
		case _ : 
			print("Invalid Input")
			print(show_menu())
