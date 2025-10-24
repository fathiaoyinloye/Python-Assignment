def get_fahrenheit(celcius):
	return celcius * 1.8 + 32
celcius = [0,20,37,100]

result = list(map(get_fahrenheit,celcius))
print(result)