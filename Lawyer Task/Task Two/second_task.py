
def find_largest(numbers):
	count = 0
	largest = numbers[0]
	for _ in numbers:
		if numbers[count] > largest:
			largest = numbers[count]
		count = count + 1
	return largest



def find_smallest(numbers):
	count = 0
	smallest = numbers[0]
	for _ in numbers:
		if numbers[count] < smallest:
			smallest = numbers[count]
		count = count + 1
	return smallest


def sum_first_middle_last_elements(numbers):
	middle_index = len(numbers)//2
	middle_element = numbers[middle_index]
	first_element = numbers[0]
	last_element = numbers[len(numbers) -1]
	sum = middle_element + first_element + last_element
	return sum




def add_third_elements(numbers):

	count = 0
	sum = 0
	for elements in numbers:
		if count % 3 == 0:
			sum += elements
		
	return sum
score = [4,6,77,3,2,5,7]
print(find_largest(score))
print(find_smallest(score))
print(sum_first_middle_last_elements(score))
print(add_third_elements(score))
