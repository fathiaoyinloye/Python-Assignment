
for number in range(5):
	count = 1
	while(count <= 5):
		count = count + 1
		print("*" ,end = " ")
	
	print(end = "\n")

print()

for column in range(1, 6):
	for row in range (column):
		print("*" , end = " ")

	print()


print()
for column2 in range(5, 0, -1):
	for row in range (column2):
		print("*" , end = " ")	

	print()

print()

for column in range(1, 6):

	for column in range(1, 6):
		for row in range (column):
			print("*" , end = " ")
	print(end = "\n")

	for column2 in range(column -1):
		for row in range (column2):
			print(" *" , end = " ")
	print(end = "\n")

