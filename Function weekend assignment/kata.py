def is_prime(number): 
	sum = 0
	prime_number = 1 + number
	for count in range(1, number + 1):
		if(number % count == 0):
			sum = sum + count

	if sum == prime_number:
		return True
	else:
		return False


def is_even (number): 
	if number % 2 == 0:
		return True
	else:
		return False


def is_odd (number): 
	if number % 2 != 0:
		return True
	else:
		return False


def factorial_of (number):
	factorial = 1
	for count in range(1, number + 1):
		factorial = factorial * count
	return factorial

def subtract(numberOne, numberTwo):
	largest = numberOne
	lowest = numberTwo
	if numberTwo > largest:
		largest = numberTwo
		lowest = numberOne
	subtract = largest - lowest
	return subtract


def divide(numberOne, numberTwo):
	if numberTwo == 0:
		return 0
	quotient = numberOne/numberTwo
	return quotient


def factor_of(number): 
	sum = 0
	for count in range(1, number + 1):
		if(number % count == 0):
			sum = sum + 1
	return sum

def is_square(number): 
	sum = 0
	for count in range(1, number + 1):
		if(number % count == 0):
			sum = sum + 1
	if sum % 2 == 0:
		return False
	else:
		return True

def is_palindrome(number):

	digit1 = number // 10000
	digit2 = (number % 10000) // 1000
	digit3 = (number % 1000) // 100
	digit4 = (number % 100) // 10
	digit5 = number % 10


	if digit1 == digit5 and digit2 == digit4:
		return True
	
	else:
		return False

def square_of(number): 
	square = number * number
	return square
	


print(is_prime(7))
print(is_even(5))
print(is_odd(5))
print(factorial_of(6))
print(subtract(7, 13))
print(divide(5, 2))
print(factor_of(9))
print(is_square(16))
print(is_palindrome(641))
print(square_of(5))




