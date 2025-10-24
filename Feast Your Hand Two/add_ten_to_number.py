def add_ten_to_number(number):
	number = number + 10
	return number

print(add_ten_to_number(10))

numbers = [2,4,1,3]



result = list(map(add_ten_to_number(numbers)))
print(result)
