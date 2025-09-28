"""
create a container called product and it should be given the value 1
create an empty container called average	
create an empty container called sum	
create an empty container called smallest	
create an empty container called largest
create a container  counter that keeps track of how many times you want to repeat an action
in this case, the action should be repeated four times
prompt the user to enter an input save as number
the number should be added to  sum

the first time the user input a number,
the number should become the smallest
the number should also become the largest
if any number inputed is lesseer than it
it should take the place of the smallest
if any number inputed is greater than it
it should take the place of the largest
multiply by product
and divide the sum by 2 to get average
print smallest
print highest
print average
print product
print sum




	


"""

product = 1
average = 0
sum = 0
smallest = 0
largest = 0

for counter in range(4):
	number =int(input("Enter a number: "))

	sum= sum + number
	
	product = product * number

	if(counter == 0):
		smallest = number
		largest = number
	if(number < smallest):
		smallest = number
	if(number > largest):
		largest = number

print("The smallest of all numbers is", smallest)

print("The largest of all numbers is", largest)

print("The sum of all numbers is", sum)

print(f"The average of the numbers is {sum/4: .1f}")

print("The product of all numbers is", product)


