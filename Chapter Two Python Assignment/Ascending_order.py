#	prompt user to input three floating point
#	find the smallest number
#	find the highest number
#	sum up the the numbers and subtract smallest and highest from the sum that would give the middle number
#	print, smallest, middle and highest number




first = float(input("Enter first decimal number: "))
second = float(input("Enter second decimal number: "))
third = float(input("Enter third decimal number: "))

smallest = first
if(second < smallest):
	smallest = second

if(third < smallest):
	smallest = third


highest = second
if(first > highest):
	highest = first

if(third > smallest):
	highest = third

median = first + second + third - smallest - highest

print(smallest, "\t" , median, "\t" , highest)