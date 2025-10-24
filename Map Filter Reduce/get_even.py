def is_even(number):
	return number % 2 == 0
numbers = [2,5,3,6,7,38,10]


result = list(filter(is_even,numbers))

print(result)