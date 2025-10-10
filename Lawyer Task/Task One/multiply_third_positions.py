
numbers = [5,3,44,6,5, 10,34]
count = 0
sum = 1
for elements in numbers:
	if count % 3 == 0:
		sum *= elements
		
print("The sum of elements at third position is ", sum)