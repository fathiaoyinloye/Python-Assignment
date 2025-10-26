numbers = ([1,2,4],2)
numbers[0].append(1)
print(numbers)

print(numbers)



elements = ["name", "fat", "boy", "fhjklug", "ladies"]
my_list = list(elements)
my_list.append("mango")
my_tuple = tuple(my_list)
print(my_tuple)


def five_characters(string):
	return len(string) > 5

result = list(filter(five_characters,elements))
print(result)


string = "madm"
print(string[ : :-1])


name = "fathia++*ghj"
for word in name:
	if word.isalpha():
		word = word.upper()
	
word = "string"
word2 = word[0].upper() + word[1:]
word = word2
print(word)