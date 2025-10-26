from functools import reduce;

def get_cummulative_square(number_one, number_two):
	
	sum = number_one  + number_two +number_one  + number_two 

	return sum
my_lists = [1,2,2]
result = reduce(get_cummulative_square,my_lists)
print(result)