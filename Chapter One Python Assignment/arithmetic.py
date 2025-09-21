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




