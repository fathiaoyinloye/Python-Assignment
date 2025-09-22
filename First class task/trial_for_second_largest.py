first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

second_highest = first_number


if (second_number > first_number and second_number < third_number):
	second_highest = second_number
	
if (third_number > first_number and third_number < second_number):
	second_highest = third_number


print("The  second highest number is: ", second_highest)
