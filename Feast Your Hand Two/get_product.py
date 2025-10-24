from functools import reduce;

def get_product(number_one, number_two):
	return number_one * number_two
my_list = [1,2,3,4,5,6]
result = reduce(get_product,my_list)
print(result)