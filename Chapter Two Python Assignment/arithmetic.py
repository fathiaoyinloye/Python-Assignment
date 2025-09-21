#	prompt user to enter three numbers
# 	add up the three numbers to get the sum
# 	divide the sum by 3 to get the average
# 	multiply the three numbers to get the product
#	to get the smallest, lets asssume that the smallest number is the first
#	if second number is lesser than smallest it becomes smallest
#  	if third number is lesser than smallest it becomes smallest
#	to get the highest, lets asssume that the largest number is the second
#	if first number is lesser than smallest it becomes smallest
#  	if third number is lesser than smallest it becomes smallest
#	print the sum, the average, the product, the smallest and largest


first_number = int (input("Enter first number: "))

second_number = int (input("Enter second number: "))

third_number = int (input("Enter third number: "))

sum = first_number + second_number + third_number
print("The sum of the numbers is ", sum)

average = sum/3
print("The average of the numbers is ", average)


product = first_number * second_number * third_number
print("The product of the numbers is ", product)


smallest = first_number

if(second_number < smallest):
	smallest = second_number

if(third_number < smallest):
	smallest = third_number

largest = second_number

if(first_number > largest):
	largest = first_number

if(third_number > largest):
	smallest = third_number

print("The smallest number is", smallest)

print("The largest number is", largest)




