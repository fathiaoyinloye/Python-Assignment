from multifuel_dispenser_system_function import *

history = []
home_display = home_menu()
print(home_display)
choice = "0";
while(choice != "2"):
	choice = input("Enter Operation: ")
	match choice:
		case "1":
			display = menu()
			print(display)
			fuel_type = input("Enter fuel type from the above menu: ").lower()
			match fuel_type:
				case "1": 
					option = input("Liter or Amount: ").lower()
					while(option != "liter" and option != "amount"):
						print("Invalid Input, Please Input liter or amount")
						input = input("Liter or Amount: ").lower()
						if input == "liter" or input == "amount":
							break

					match option:
						case "liter": 
							liters = int(input("How many liters of petrol are you buying(350/L): "))
							output = calculate_total_cost("Petrol", liters,350,history)
							print(output)
							print(home_display)

						case "amount":
							amount = int(input("How much Petrol Are You Buying(350/L): "))
							output = calculate_liters("Petrol", amount,350,history)
							print(output)
							print(home_display)
					

				case "2":
					choice = input("Liter or Amount: ").lower()
					match choice:
						case "liter": 
							liter = int(input("How many liters of Diesel are you buying(400/L): "))
							output = calculate_total_cost("Diesel", liter,400,history)
							print(output)
						case "amount":
							amount = int(input("How much Diesel Are You Buying(400/L): "))
							output = calculate_liters("Diesel", amount,400,history)
							print(output)

				case "3":
					choice = input("Liter or Amount: ").lower()
					match choice:
						case "liter": 
							liter = int(input("How many liters of Kerosene are you buying(500/L): "))
							output = calculate_total_cost("Kerosene", liter,500,history)
							print(output)
						case "amount":
							amount = int(input("How much Kerosene Are You Buying(500/L): "))
							output = calculate_liters("Kerosene", amount,500,history)
							print(output)

				case "4":
					choice = input("Liter or Amount: ").lower()
					match choice:
						case "liter": 
							liter = int(input("How many liters of Gas are you buying(650/L): "))
							output = calculate_total_cost("Gas", liter,650,history)
							print(output)
						case "amount":
							amount = int(input("How much Gas Are You Buying(650/L): "))
							output = calculate_liters("Gas", amount,650,history)
							print(output)
				case _: print("Invalid Input")



		case "2":
			output = show_transactions(history)
			print(output)
		case _ : print("Invalid Input")
