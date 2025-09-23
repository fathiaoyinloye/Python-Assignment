first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

fourth_number = int(input("Enter fourth number: "))

sum = first_number + second_number + third_number + fourth_number

print("The sum of all numbers is ", sum)

mean = sum//4

print("The mean of the numbers is ", mean)
number1 = first_number
number4 = fourth_number

if(second_number <  number1):
	number1 = second_number

if(third_number <  number1):
	number1 = third_number

if(fourth_number <  number1):
	number1 = fourth_number


if(second_number >  number4):
	number4 = second_number

if(third_number >  number4):
	number4 = third_number

if(first_number >  number4):
	number4 = fourth_number


median = (sum - (number1 + number4)) // 2
print( "The median of the number is ", median)
