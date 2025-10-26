from functools import reduce
def concatenate_strings(word,words):
	return word + "" + words



my_list = ["Hello", " ", "World" ," ", "I", " ", "am", " ", "here", " ", "to", " ", "rule"]

result = reduce(concatenate_strings,my_list)
print(result)

