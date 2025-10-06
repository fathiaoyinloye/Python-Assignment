def only_floats(a, b):
	if a % 1 != 0 and b % 1 != 0:
		return 2
	elif   a % 1 != 0 and b % 1 == 0:

		return 1
	elif   a % 1 == 0 and b % 1 != 0:

		return 1

	else:
		return 0

	 

print(only_floats(9, 5.1))