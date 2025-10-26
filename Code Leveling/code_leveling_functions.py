def append_to_tuple(numbers,number):
	numbers[0].append(number)
	return numbers


def change_element(numbers):
	numbers[2][1] = 99
	return numbers

def covert_tuple_to_list_to_tuple(my_tuple):
	my_list = list(my_tuple)
	my_list.append("mango")
	my_new_tuple = tuple(my_list)
	return my_new_tuple


def unpack_tuple(my_tuple):
	a,b, *others = my_tuple
	return a,b, *others

def is_even(number):
	return number % 2 == 0

def even_from_one_to_twenty():
	my_list = list(range(1,21))
	result = list(filter(is_even,my_list))
	return result

def five_characters(string):
	if len(string) > 5:
		return string

def extract_word_with_more_than_five_characters(my_list):
	
	result = list(filter(five_characters,my_list))
	return result

def value_greater_than_two(my_tuple):
	if my_tuple[0] > 2:
		return my_tuple
def values_greater_than_two(my_list):
	result = list(filter(value_greater_than_two,my_list))
	return result

def is_divisible_by_three_and_five(number):
	if number % 3 == 0 and number % 5 == 0:
		return number

def they_are_divisible_by_three_and_five():
	my_list = list(range(1,51))
	result = list(filter(is_divisible_by_three_and_five,my_list))
	return result


def is_not_palindrome(word):
	if word != word[ : : -1]:
		return word
def they_are_not_palindrome(my_list):
	result = list(filter(is_not_palindrome, my_list))
	return result

def convert_to_upper_case(string):
	return string.upper()

def convert_strings_to_uppercase(my_list):
	result = list(map(convert_to_upper_case, my_list))
	return result
