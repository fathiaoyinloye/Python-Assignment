from get_generated_numbers import *

greetings ="""
*********************************************************
*	Welcome Victorious Jewel!!!			*
*	Let Go On A Muliplication Table Merry Go Round	*
*	Get Ready For A Fantastic Ride			*
*	Fasten Your Seatbelt				*
*	Bring Out The Genius in You			*
*********************************************************
"""
print(greetings)
options ="""
*********************************************************
*	Choose The Level You Want To Ride On		*
*********************************************************
*		No		Level			*
*		1 		Easy			*
*		2		Difficult		*
*********************************************************
"""


print(options)
choice = input("Choose the level: ")

if choice == "1":
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
elif choice == "2":
	generated_numbers = generate_number_two()
	product = generated_numbers[0] * generated_numbers[1]
	user_input = 0
	while(user_input != -1):
		user_input = int(input(f"How much is {generated_numbers[0]} times {generated_numbers[1]} : "))
		if user_input == product:
			print(generate_correct_response())
			print("Please enter -1 to stop or answer the question to continue")
			generated_numbers = generate_number_two()
			product = generated_numbers[0] * generated_numbers[1]
		
		elif user_input != product and user_input != -1 :
			print(generate_incorrect_response())
else:
	print("Please enter a correct choice of either 1 or 2")
