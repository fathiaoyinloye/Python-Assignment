five_digit_number = int (input("Enter a five digit number: "))


digit1 = five_digit_number // 10000
digit2 = (five_digit_number % 10000) // 1000
digit3 = (five_digit_number % 1000) // 100
digit4 = (five_digit_number % 100) // 10
digit5 = five_digit_number % 10


if(five_digit_number < 9999 or five_digit_number >= 100000):
	print("Invalid input, please input a five digits number")


else:

	print(digit1, "\t", digit2, "\t", digit3, "\t", digit4, "\t", digit5)
