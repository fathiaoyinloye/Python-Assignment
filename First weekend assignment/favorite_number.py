# create a variable favorite number an assign 7 to it
# prompt user to guess a number
# if guessed number is is 7
# print That's my favorite number, if not
# print Nice try, guess again!


favorite_number = 7

guess = int (input("Guess a number: "))

if(guess == 7):
	print("That's my favorite number: ")

else:
	print("Nice try, guess again!")