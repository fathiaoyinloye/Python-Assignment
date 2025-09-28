count = 0
largest =  0
largestTwo = 0
while(count < 10):
	number = int(input("enter a number: "))
	count = count + 1
	if count == 0:
		largest = number

	if count == 1:
		largestTwo = number

	if number > largest:
		largest = number

	if number > largest and number > largestTwo:
		largestTwo = number

	print(largest, largestTwo)

print(largest,largestTwo)

