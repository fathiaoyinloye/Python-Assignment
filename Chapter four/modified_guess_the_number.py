my_number = 32

guess = 0
number_of_guess = 0;
while (guess != -1):

	guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
	
	if guess == my_number:
		if number_of_guess <= 10:
			print("Either you knows the secret or you got lucky")
		print("You guessed the number")
		print("Click on -1 to end the game or any number to continue: ")

	elif guess > my_number:
		print("Too High. Try Again.")
		number_of_guess += 1
		
	elif guess > 0:
		print("Too Low. Try Again.")
		number_of_guess += 1
		
