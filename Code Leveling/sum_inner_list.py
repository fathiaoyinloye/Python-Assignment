from functools import reduce
def sum(x,y):
	return x + y
new_number = []
numbers = [[2,3,4], [1,5,7], [4,6,8]]
for element in numbers:
	result = reduce(sum, element)	
	new_number.append(result)



def get_sum(number_1, number2):
	return number_1 + number2


def sum_inner_list(two_D_List):
	new_list = []
	for element in two_D_List:
		new_number.append(reduce(get_sum, element))
	return new_number
	

number = [[2,3,4], [1,5,7], [4,6,8]]

print(sum_inner_list(number))