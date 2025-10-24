def add_ten_to_number(number):
	return number + 10

numbers = [2,4,1,3]


result = list(map(add_ten_to_number,numbers))
print(result)
