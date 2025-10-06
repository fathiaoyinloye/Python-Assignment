digit = 0
number = 15
reverseNumber = 0
multiplier = 10
numberToCheck = number
count = 1
while number > 0:
	digit = number % 10
	reverseNumber = reverseNumber * multiplier + digit
	if count == 1:
		reverseNumber = digit * 1
			
	print(reverseNumber)
	count = count + 1
	number = number/10


if (numberToCheck == reverseNumber):
	System.out.println("Its a Palindrome");
else:
	System.out.print("Its not a Palindrome");
	


