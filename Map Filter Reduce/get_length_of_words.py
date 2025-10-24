def  get_length(word):
	return len(word)

words = ["Monday", "Fathia", "Haliyah", "Pen"]

result = list(map(get_length, words))


print(result)