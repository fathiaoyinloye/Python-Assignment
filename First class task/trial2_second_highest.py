first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

highest = first_number
lowest = second_number


if (second_number > highest):
	highest = second_number


if (third_number > highest):
	highest = third_number


if (first_number < lowest):
	lowest = first_number


if (third_number < lowest):
	lowest = third_number

sum = first_number + second_number + third_number
second_highest = sum - highest - lowest
print("The  second highest number is: ", second_highest)
