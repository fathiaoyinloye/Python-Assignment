def access_third_element (numbers):
	for number in numbers:
		third_element = numbers[2]
		
		return third_element



def change_last_element(elements):
	for element in elements:
		elements[-1] = "Yellow"
	return elements

def append_element(elements):
	elements.append("Purple")
	return elements


def remove_element(elements):
	elements.remove(elements[2])
	return elements

def return_length_of_list(elements):
	list = []
	count = 0
	for element in elements:
		length = len(elements[count])
		list.append(length)
		count += 1
	return list

def return_even_numbers(elements):
	evenNumbers = []
	count = 0
	for _ in elements:
		if elements[count] % 2 == 0:
			evenNumbers.append(elements[count])
		count += 1
	return evenNumbers
def join_two_elements(elements_one, element_two):
	elements_one += element_two
	return elements_one



def more_than_three_characters(elements):
	list = []
	count = 0
	for element in elements:
		if len(elements[count]) >= 3:
			list.append(elements[count])
		count += 1
	return list

def ascending_order(elements):
	elements.sort()
	return elements
	


colors = ["red", "green", "blue"]
my_list = [1,3,467,7,6,4,9]
"""
print(access_third_element(my_list))
print(change_last_element(colors))
print(change_last_element(colors))
print(append_element(colors))

print(remove_element(colors))
print(return_length_of_list(colors))
print(join_two_elements(colors, my_list))
"""
print(ascending_order(my_list))
