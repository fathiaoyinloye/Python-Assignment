from get_generated_numbers import *

print(print_options())
choice = input("Enter your choice of Arithmetic Operation: ")
match choice:
	case "1" : 
		print(choose_level())
		level = input("Choose level of your choice: ")
		match level:
			case "1":
				generated_numbers = generate_number()
				addition = generated_numbers[0] + generated_numbers[1]
				user_input = 0
				while(user_input != -1):
					user_input = int(input(f"How much is {generated_numbers[0]} plus {generated_numbers[1]} : "))
					if user_input == addition:
						print(generate_correct_response())
						print("Please enter -1 to stop or answer the question to continue")
						generated_numbers = generate_number()
						addition = generated_numbers[0] + generated_numbers[1]
		
					elif user_input != addition and user_input != -1 :
						print(generate_incorrect_response())
			case "2": 
				generated_numbers = generate_number_two()
				addition = generated_numbers[0] + generated_numbers[1]
				user_input = 0
				while(user_input != -1):
					user_input = int(input(f"How much is {generated_numbers[0]} plus {generated_numbers[1]} : "))
					if user_input == addition:
						print(generate_correct_response())
						print("Please enter -1 to stop or answer the question to continue")
						generated_numbers = generate_number_two()
						addition = generated_numbers[0] + generated_numbers[1]
		
					elif user_input != addition and user_input != -1 :
						print(generate_incorrect_response())



			case _ :
				print("Invalid Input")
				print(choose_level())
				level = input("Choose level of your choice: ")


	case "2" : 
		print(choose_level())
		level = input("Choose level of your choice: ")
		match level:
			case "1":
				generated_numbers = generate_number()
				subtraction = generated_numbers[0] - generated_numbers[1]
				user_input = 0
				while(user_input != -1):
					user_input = int(input(f"How much is {generated_numbers[0]} minus {generated_numbers[1]} : "))
					if user_input == subtraction:
						print(generate_correct_response())
						print("Please enter -1 to stop or answer the question to continue")
						generated_numbers = generate_number()
						subtraction = generated_numbers[0] - generated_numbers[1]
		
					elif user_input != subtraction and user_input != -1 :
						print(generate_incorrect_response())
			case "2": 
				generated_numbers = generate_number_two()
				subtraction = generated_numbers[0] - generated_numbers[1]
				user_input = 0
				while(user_input != -1):
					user_input = int(input(f"How much is {generated_numbers[0]} minus {generated_numbers[1]} : "))
					if user_input == subtraction:
						print(generate_correct_response())
						print("Please enter -1 to stop or answer the question to continue")
						generated_numbers = generate_number_two()
						subtraction = generated_numbers[0] - generated_numbers[1]
		
					elif user_input != subtraction and user_input != -1 :
						print(generate_incorrect_response())



			case _ :
				print("Invalid Input")
				print(choose_level())
				level = input("Choose level of your choice: ")






	case "3" : 
		print(choose_level())
		level = input("Choose level of your choice: ")
		match level:
			case "1":
				generated_numbers = generate_number()
				product = generated_numbers[0] * generated_numbers[1]
				user_input = 0
				while(user_input != -1):
					user_input = int(input(f"How much is {generated_numbers[0]} times {generated_numbers[1]} : "))
					if user_input == product:
						print(generate_correct_response())
						print("Please enter -1 to stop or answer the question to continue")
						generated_numbers = generate_number()
						product = generated_numbers[0] * generated_numbers[1]
		
					elif user_input != product and user_input != -1 :
						print(generate_incorrect_response())
			case "2": 
				generated_numbers = generate_number_two()
				product = generated_numbers[0] * generated_numbers[1]
				user_input = 0
				while(user_input != -1):
					user_input = int(input(f"How much is {generated_numbers[0]} times {generated_numbers[1]} : "))
					if user_input == product:
						print(generate_correct_response())
						print("Please enter -1 to stop or answer the question to continue")
						generated_numbers = generate_number_two()
						product = generated_numbers[0] - generated_numbers[1]
		
					elif user_input != product and user_input != -1 :
						print(generate_incorrect_response())



			case _ :
				print("Invalid Input")
				print(choose_level())
				level = input("Choose level of your choice: ")



	case "4" : print("division")
	case _ : print("Invalid Input")




