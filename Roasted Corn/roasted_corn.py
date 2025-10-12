def remove_odd_index(name):
	output = ""
	for count in range (1, len(name) , 2):
		output = output + name[count]
	return output 

def add_suffix(name):
	new_name = ""
	check_ing = ""
	check_ly = ""
	for count in range (-1, -len(name) , -1):
		check_ing = name[count] + check_ing
		if count == -3:
			break
	for count in range (-1, -len(name) , -1):
		check_ly = name[count] + check_ly
		if count == -2:
			break



	if len(name) >= 3 and check_ing != "ing" and check_ly != "ly":
		name = name + "ing"

	elif len(name) >= 3 and check_ing == "ing":
		for count in range(0, len(name)-3, 1):
			new_name = new_name + name[count]	
		name = new_name  + "ly"

	elif len(name) >= 3 and check_ly == "ly":
		for count in range(0, len(name)-2, 1):
			new_name = new_name + name[count]	
		name = new_name  + "ing"
	else:
		name = name

	return name


def two_first_last_characters(name):
	if len(name) > 1:
		output = name[0] + name[1] + name [len(name)- 2] + name [len(name)- 1]
	else: 
		output = '""'
	return output


def characters_multiples(letters, number):
	output = ""
	if number % 1 == 0:
		for _ in range (number + 1):
			output += letters
	else:
		output = letters
	
	return	output



def get_squares(numbers):
	count = 0
	for _ in numbers:
		numbers[count] = numbers[count]**2
		count = count + 1
	return numbers


def get_sum_of_squares (numbers):
	count = 0
	for _ in numbers:
		numbers[count] = numbers[count]**2
		count = count + 1
	index = 0
	sum = 0
	for _ in numbers:
		sum = sum + numbers[index]
		index += 1
	return sum

def get_longest_words(name):
	count = 0
	longest = len(name[0])
	longest_word = ""
	for characters in name:
		if len(name[count]) > longest:
			longest = len(name[count])
			longest_word = name[count]
		count = count + 1
		
	result = [longest, longest_word]
	return result
def get_minimum_number (numbers):
	minimum = numbers[0] 
	count = 0
	for _ in numbers:
		if numbers[count] < minimum:
			minimum = numbers[count]
		count += 1
	return minimum

def get_maximum_number (numbers):
	maximum = numbers[0] 
	count = 0
	for _ in numbers:
		if numbers[count] > maximum:
			maximum = numbers[count]
		count += 1
	return maximum