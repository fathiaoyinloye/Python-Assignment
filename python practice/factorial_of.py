def factorial_of (number):
	factorial = 1
	for count in range(1, number + 1):
		factorial = factorial * count
	return factorial



number = int(input("Enter a number: "))
print(factorial_of(number))
