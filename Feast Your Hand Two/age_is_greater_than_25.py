
def age_is_greater_than_25(my_dictionary):
	my_list = []
	for key,value in my_dictionary.items():
		if value > 25:
			my_list.append((key,value))
	return my_list

my_dictionary = {"Alice": 23, "Bayo": 28, "Nissi": 50, "Ekwe": 67}age_is_greater_than_25(my_dictionary))

"""result = filter(age_is_greater_than_25, my_dictionary);

print(result);
"""