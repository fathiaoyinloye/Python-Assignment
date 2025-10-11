name = "stup"

"""new_name = ""
check_ing = ""
check_ly = ""
for count in range (-1, -len(name) , -1):
	check_ing = name[count] + check_ing
	if count == -3:
		break
for count in range (-1, -len(name) , -1):
	check_ly = name[count] + check_ly
	if count == -2:
		break



if len(name) >= 3 and check_ing != "ing" and check_ly != "ly":
	name = name + ing

elif len(name) >= 3 and check_ing == "ing":
	for count in range(0, len(name)-3, 1):
		new_name = new_name + name[count]	
	name = new_name  + "ly"

elif len(name) >= 3 and check_ly == "ly":
	for count in range(0, len(name)-3, 1):
		new_name = new_name + name[count]	
	name = new_name  + "ing"
else:
	name = name

print(name)

#output = ""
#for count in range (1, len(name) , 2):
if len(name) > 1:
	output = name[0] + name[1] + name [len(name)- 2] + name [len(name)- 1]
else: 
	output = '""'
print(output)

output = ""
number = 2.5
if number % 1 == 0:
	for _ in range (number + 1):
		output += name
else:
	output = name
	
print(output)
""" 
numbers = [3,5,6,7]
count = 0
for _ in numbers:
	numbers[count] = numbers[count]**2
	count = count + 1
print(numbers)
index = 0
sum = 0
for _ in numbers:
	sum = sum + numbers[index]
	index += 1
	print(sum)
	

