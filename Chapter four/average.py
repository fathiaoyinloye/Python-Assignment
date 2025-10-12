def average (numbers):
	sum = 0 
	count = 0
	for _ in numbers:
		sum += numbers[count]
		count += 1
		average = sum/count
	return average
numbers = [2,5,7,3]
print(average(numbers))