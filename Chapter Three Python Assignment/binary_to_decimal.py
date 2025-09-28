"""	prompt a user to enter a number that is in 0 and 1
	save it as binary
	create an empty container and name it decimal
	create a container, name it count and it should be equal to 1
	create an empty container and name it digit
	
	while inputed number (binary) is greater  than zero
	digit should be equal to the reminder of binary divided by 10
	digit should multiply count and be added to decimal then reassign to decimal
	binary should then become binary divided by 10
	count should also be multiplied by 2
	print  the decimal
	
"""
binary = int(input("Enter a number that is in 0's and 1: "))
decimal = 0
count = 1
digit = 0

while(binary > 0):
	digit = binary % 10;
	decimal = decimal +  (digit * count);
	binary = binary//10;
	count = count * 2;
print("The inputed number in decimal is" , decimal)