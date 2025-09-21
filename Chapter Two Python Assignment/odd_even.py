#prompt user to enter a number
# if number divided by 2 gives no remainder print it as an even number
# if not, it is an odd number


number = int (input("Enter any number: "))

if(number % 2 == 0):
	print(number,"is an even number")

else: 
	print(number,"is not an even number ")
	