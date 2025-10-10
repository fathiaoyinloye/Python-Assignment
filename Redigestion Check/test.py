def get_reverse (characters):
	number = 0
	sum_reverse = " "
	for _ in characters:
		number = number - 1	
		sum_reverse += characters[number]

	return sum_reverse

print(get_reverse("bnbv"))


hour = 20
minute = 10
name = "The hour is: " + str(hour) + str(minute)
print(name)


sum_a = 0;
sum_e = 0;
sum_i = 0;
sum_o = 0;
sum_u = 0;

for character in "lettersaeii":
	if character == "e":
		sum_e += 1
		if sum_e > 1:
			sum_e = sum_e - 1
	if character == "a":
		sum_a += 1
		if sum_a > 1:
			sum_a = sum_a - 1

	if character == "i":
		sum_i += 1
		if sum_i > 1:
			sum_i = sum_i - 1

	if character == "o":
		sum_o += 1
		if sum_o > 1:
			sum_o = sum_o - 1

	if character == "u":
		sum_u += 1
		if sum_u > 1:
			sum_u = sum_u - 1
	even_occurence = sum_e + sum_i + sum_o + sum_a + sum_u
print(even_occurence)