#prompt user to enter a number
# if number divided by 2 gives no remainder print it as an even number
# if not, it is an odd number

number = int (input("Enter a number: "))

if (number % 2 == 0):
	print(number, "is an Even number")

else:
	print(number, "is an Odd number")
