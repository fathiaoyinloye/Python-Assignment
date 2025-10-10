def find_smallest(numbers):
	count = 0
	smallest = numbers[0]
	for _ in numbers:
		if numbers[count] < smallest:
			smallest = numbers[count]
		count = count + 1
	return smallest

def find_average(numbers):
	sum = 0
	average = 0
	for element in numbers:
		sum = sum + element
		average = sum/len(numbers)	
	return average



def count_occurence(numbers,number):
	count = 0
	occurred = 0
	for _ in numbers:
		if numbers[count] == number:
			occurred += 1
		count += 1
	return occurred

def contains_element(numbers,number):
	count = 0
	occurred = 0
	for element in numbers:
		if numbers[count] == number:
			occurred += 1
		count += 1
	if occurred > 0:
		return True
	elif occurred == 0:
		return False

def get_first_element(numbers):
	first = 0
	if numbers == []:
		return 0
	else:
		first = numbers[0]
		return first
	

def get_last_element(numbers):
	last = 0
	if numbers == []:
		return 0
	else:
		last = numbers[len(numbers)-1]
		return last

def list_length(numbers):
	count = 0
	for _ in numbers:
		count += 1
	return count


def get_middle_element(numbers):
	middle_element = 0;
	if len(numbers) % 2 == 0:
		middle_index = len(numbers)//2 - 1
	else: 
		middle_index = len(numbers)//2

	middle_element = numbers[middle_index]
		
	return middle_element

def swap_first_and_last(numbers):
	for element in numbers:
		first = numbers[0]
		numbers[0] = numbers[len(numbers)-1]
		numbers[len(numbers)-1] = first
		return numbers

score = [5,2,1,4,5,6,4,6]
test = []
print(find_smallest(score))
print(find_average(score))
print(count_occurence(score, 2))
print(contains_element(score, 12))
print(get_first_element(score))
print(get_last_element(test))
print(list_length(test))
print(get_middle_element(score))
print(swap_first_and_last(score))
