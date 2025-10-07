number = input("Enter a number: ")
digit = 0
number2 = int (number) 
reverseNumber = 0
multiplier = 10
numberToCheck = number2

digit 
#print(len(number)) 
for count in range(len(number)):
		digit = number2 % 10
		number2 = number2//10
		reverseNumber = reverseNumber * multiplier + digit
		if(count == 0):
			reverseNumber = digit * 1
if(reverseNumber == numberToCheck):
	print("It's a Palindome")
else:
	print("It's not Palindome")
