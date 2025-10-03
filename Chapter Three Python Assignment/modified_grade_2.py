passes = 0  
failures = 0 
count = 0

result = int(input('Enter result (1=pass, 2=fail): '))
while count < 10:
	if result != 1 or result != 2:
		
	elif result == 1:
		passes = passes + 1
		count = count + 1
	elif result == 2:
		failures = failures + 1
		count = count + 1
	else: 
		print ("invalid input")
		result = int(input('Enter result (1=pass, 2=fail): '))
print('Passed:', passes)

print('Failed:', failures)

if passes > 8:
		print("Bonus to instructor")
	
