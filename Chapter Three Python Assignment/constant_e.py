e = 1
count = 1
factorial = count
numerator = 1
while(count <= 10):
	factorial = factorial * count
	x = numerator/factorial
	e = e +  x

	count = count + 1

	print(f"{x: .2f},  {e: .2f}")


