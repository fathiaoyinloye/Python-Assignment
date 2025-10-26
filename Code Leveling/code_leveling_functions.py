from functools import reduce


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


def convert_first_letter_to_uppercase(word):
	word2 = word[0].upper() + word[1:]
	word = word2
	return word


def convert_first_letters_in_a_list_to_uppercase(my_list):
	result = list(map(convert_first_letter_to_uppercase, my_list))
	return result

def add_ten_percent_to_price(price):
	return price + price * 10//100

def add_ten_percent_of_tax_to_prices(prices):
	result = list(map(add_ten_percent_to_price,prices))
	return result


def get_sum(number_1, number2):
	return number_1 + number2

def get_sum_one_to_hundred():
	my_list = list(range(1,51))
	result = reduce(get_sum, my_list)
	return result
def get_maximum(number_1, number_2):
	maximum = number_1
	if number_2 > maximum:
		maximum = number_2
	return maximum
def get_maximum_numbers(my_list):
	result = reduce(get_maximum,my_list)
	return result

def get_squares(number):
	return number*number

def get_product(number_1, number_2):
		return number_1 * number_2

def get_squares_and_product_of_squares(my_list):
	result_1 = list(map(get_squares,my_list))
	result_2 = reduce(get_product,result_1)
	return result_2

def get_number_greater_than_five(number):
	return number > 5

	
def sum_inner_list(two_D_List):
	new_list = []
	for element in two_D_List:
		new_list.append(reduce(get_sum, element))
		
	return new_list


def get_sum_greater_than_five(my_list):
	result_1 = sum_inner_list(my_list)
	result_2 = list(filter(get_number_greater_than_five,result_1))
	return result_2


def get_letter(my_list):
	new_list = []
	for element in my_list:
		if element.isalpha():
			new_list.append(element)
		
	return new_list

def convert_letter_to_number(word):
	return ord(word)

def get_letter_convert_to_numbers(my_list):
	my_number_list = []
	result_1 = get_letter(my_list)
	for element in result_1:
		result = list(map(convert_letter_to_number, element))
		my_number_list.append(result)
	return my_number_list

def get_sum_of_converted_numbers(my_list):
	result_1 = get_letter_convert_to_numbers(my_list)
	result_2 = sum_inner_list(result_1)
	return result_2


def concatenate_strings(word,words):
	return word + " " + words

def concatenate_series_of_strings(my_list):
	result = reduce(concatenate_strings,my_list)
