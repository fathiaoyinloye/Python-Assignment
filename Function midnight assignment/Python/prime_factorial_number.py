number = int(input("Enter a number: "))
sum = 0
prime_number = 1 + number
factorial = 1
for count in range(1, number + 1):
	factorial = factorial * count
	if(number % count == 0):
		sum = sum + count

if sum == prime_number:
	print("It's a prime number")
else:
	print("It's not prime number")

	
print(factorial)