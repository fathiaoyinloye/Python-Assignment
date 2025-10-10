
def gives_length(character):
	number = 0
	for _ in character:
		number = number + 1	


	return number


def get_reverse (characters):
	number = 0
	sum_reverse = ""
	for _ in characters:
		number = number - 1	
		sum_reverse += characters[number]

	return sum_reverse





def get_seconds_hour(minutes):
	hour = minutes//60
	seconds = minutes * 60
	
	output = "The inputed " + str(minutes) + "minutes is equivalent to " + str(hour) + "hour" + " and also equivalent to " + str(seconds) + "seconds"
	return output


def count_vowels(input):
	sum_a = 0;
	sum_e = 0;
	sum_i = 0;
	sum_o = 0;
	sum_u = 0;

	for character in input:
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
	return even_occurence


print(gives_length("number"))
print(get_seconds_hour(1000))
print(get_reverse("baby"))
print(count_vowels("baaiiioooooaby"))
