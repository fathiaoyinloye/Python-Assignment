
numbers = [1,3,44,6,5, 10,34]
count = 0
sum = 0
for elements in numbers:
	if count % 2 != 0:
		sum += elements
	count += 1

	
print("The sum of elements at even position is ", sum)