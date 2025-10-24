from functools import reduce

def concatenate_strings(word1,word2):
	return word1 + " - " + word2

words = ["fat", "boy", "girl", "computer"]
result = reduce(concatenate_strings,words)



result = list(enumerate(words))
print(result)