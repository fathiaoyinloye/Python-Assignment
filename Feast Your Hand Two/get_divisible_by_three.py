def get_divisible_by_three(number):
	if number % 3 == 0:
		return number;
my_list = [1,2,4,6,9,12]

result = list(filter(get_divisible_by_three,my_list))
print(result) 