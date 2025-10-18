import random
car = ["toyota", "camry" ,"benz"]
random.shuffle(car)
randomNumber = random.choice(car)

choice = "tota"
new = "lexus"
if choice in car:
	car.remove(choice)
	car.append(new)
	
else:
	print("Invalid")


print(car)
"""
choice = "book"
car.append(choice)
	
for element in car:
	print(element)
my_list = [1,2,4,5,7,8,6,2,3,4]
y_list.sort()
my_car[element for element in car]
print(my_car)"""
