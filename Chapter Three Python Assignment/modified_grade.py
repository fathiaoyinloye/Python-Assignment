passes = 0  

failures = 0 
count = 0
while count < 10:
	result = int(input('Enter result (1=pass, 2=fail): '))
	
	
	if result == 1:
		passes = passes + 1
		count = count + 1
	elif result == 2:
		failures = failures + 1
		count = count + 1
	else: 
		continue;	
	
	print('Passed:', passes)

	print('Failed:', failures)

	if passes > 8:
		print("Bonus to instructor")
	
