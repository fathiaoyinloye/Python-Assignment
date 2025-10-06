digit = 0
number = 152
reverseNumber = 0
multiplier = 10
numberToCheck = number
count = 5
while(number > 0 ):
	digit = number % 10
	number = number // 10
	reverseNumber = reverseNumber * multiplier + digit
	if (count == 5):
		reverseNumber = digit * 1
	
	count += 1
	print(reverseNumber)
	
if (numberToCheck == reverseNumber):
	print("Its a Palindrome")
else:
	print("Its not a Palindrome")

	
