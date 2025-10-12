def get_product(*numbers):
	product = 1
	for number in  numbers:
		product *= number
	return product
print(get_product(4,6,7,5))
print(get_product(78,38,2,4,8,9,4,6,7,5))
print(get_product(59,23,45,7,35,8,38,2,4,8,9,4,6,7,5))