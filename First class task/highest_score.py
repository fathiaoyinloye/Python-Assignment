first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

highest = first_number


if (second_number > highest):
	highest = second_number


if (third_number > highest):
	highest = third_number


print("The highest number is: ", highest)

