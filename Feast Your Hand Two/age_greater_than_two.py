
def age_is_greater_than_25(my_dictionary):
		if my_dictionary["age"] > 25:
			return my_dictionary



		
my_dictionary = {"age": 23, "age": 28, "age": 50, "age": 67}

result = list(filter(age_is_greater_than_25, my_dictionary))

print(result)
