def is_palindrome_prime(number):
	prime_number = 1 + number
	sum = 0
	for count in range(1, number + 1):
		if(number % count == 0):
			sum = sum + count

	if sum == prime_number:
		prime_number = True
	else:
		prime_number = False

	digit = 0
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
	
	if (numberToCheck == reverseNumber):
		palindrome = True
	else:
		palindrome = False


	if (palindrome == True and prime_number == True):
		return True
	else:
		return False

print(is_palindrome_prime(22))