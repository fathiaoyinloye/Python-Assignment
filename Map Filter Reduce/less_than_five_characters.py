def get_characters_less_than_five(word):
	if len(word) <= 5:
		return word

words = ["boy", "girl", "apple", "aeroplane", "Haliyah"]

result = list(filter(get_characters_less_than_five,words))

print(result)