def get_fahrenheit (celcius):
	fahrenheit = (9/5) * celcius + 32
	return fahrenheit


top = """ 
*********************************
Celcius		Fahrenheit	*
*********************************				
"""
print(top)
for number in range(0, 101):
	print(number,"\t\t", round(get_fahrenheit(number), 2), "\t\t*")
	print("*********************************")