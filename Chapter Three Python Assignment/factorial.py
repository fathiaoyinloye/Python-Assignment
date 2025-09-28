"""
prompt user to enter a number
save in a container called number
create another container which will be equal to the inputed number and call it count
count will keep count of how many times an action is to be repeated
create another container which will be equal to one and call it factorial
as long as count is greater than zero
factorial should be multiply by count continously
count should decrease by one in every of the repetition
print factorial

"""


number = int(input("Enter a number: "))
count = number
factorial = 1

while(count > 0):
	factorial = factorial * count
	count = count - 1

print("The factorial of", number, "is", factorial)
