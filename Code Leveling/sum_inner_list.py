from functools import reduce
def sum(x,y):
	return x + y
new_number = []
numbers = [[2,3,4], [1,5,7], [4,6,8]]
for element in numbers:
	result = reduce(sum, element)	
	new_number.append(result)

print(new_number)


def sum_inner_list(two_D_List):
	new_list = []
	for element in two_D_List:
		new_list.append(reduce(sum, element))
		
	return new_list
	
def get_letter(my_list):
	new_list = []
	for element in my_list:
		if element.isalpha():
			new_list.append(element)
		
	return new_list


my_list = ['123', '456', '789', 'abc', 'def']
print(get_letter(my_list))


def convert_letter_to_number(word):
	return ord(word)
result = list(map(convert_letter_to_number, "def"))
print(result)