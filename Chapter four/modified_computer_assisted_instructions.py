from get_generated_numbers import *

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