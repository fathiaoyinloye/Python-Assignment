def removeBoolean(number):
	if type(number) == int:
	 	return number

my_list = [1,3,None,6,None]


result = list(filter(removeBoolean,my_list))
print(result)