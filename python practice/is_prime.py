def is_prime(number): 
	sum = 0
	prime_number = 1 + number
	for count in range(1, number + 1):
		if(number % count == 0):
			sum = sum + count

	if sum == prime_number:
		return True
	else:
		return False


number = int(input("Enter a number: "))
print(is_prime(number))
