def get_positive(number):
	if number > -1:
		return number

my_list = [1,2,4,-5,6,9,12,-4]

result = list(filter(get_positive,my_list))
print(result) 