def  get_square(numbers):
	return numbers * numbers


numbers = [2,3,1,4,7,]

result = list(map(get_square,numbers))

print(result)