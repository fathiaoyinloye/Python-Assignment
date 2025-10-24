def convert_to_int(string):
	return int(string)

my_list = ["1", "2", "3", "4"]

result = list(map(convert_to_int, my_list))
print(result)
