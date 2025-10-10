import random


numbers = []
for _ in range(11):
	random_numbers = random.randrange(1,51)
	numbers.append(random_numbers)

print(numbers)
