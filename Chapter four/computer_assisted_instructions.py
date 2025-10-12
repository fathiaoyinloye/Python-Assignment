from get_generated_numbers import generate_number

generated_numbers = generate_number()
product = generated_numbers[0] * generated_numbers[1]
user_input = 0
while(user_input != -1):
	user_input = int(input(f"How much is {generated_numbers[0]} times {generated_numbers[1]} : "))
	if user_input == product:
		print("Very Good!, Please enter -1 to stop or answer the question to continue")
		generated_numbers = generate_number()
		product = generated_numbers[0] * generated_numbers[1]
		if user_input == -1:
			print("You've done well!!! You can even do better in another trial.")
	elif user_input != product and user_input != -1 :
		print("Please, Try Again.")
