print("numbers\t\t square\t\tcube")
for counter in range(6):
	square = counter * counter
	cube = counter * counter * counter
	print(f"{counter: .0f}\t\t{square: .0f}\t\t{cube: .0f}")