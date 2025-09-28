number = int(input("Enter a five digit number: "))



digit1 = number // 10000
digit2 = (number % 10000) // 1000
digit3 = (number % 1000) // 100
digit4 = (number % 100) // 10
digit5 = number % 10

if number <= 9999 or number >= 1000000:
	print("Invalid digit: Please enter a five digit number")

elif digit1 == digit5 and digit2 == digit4:
	print("The inputed number", number, "is a Palindrome")
	
else:
	print("The inputed number", number, "is not a Palindrome")


	

	