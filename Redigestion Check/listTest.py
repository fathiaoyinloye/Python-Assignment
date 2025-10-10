import random




numbers = []
for _ in range(11):
	random_numbers = random.randrange(1,51)
	numbers.append(random_numbers)
print(numbers)

'''for numbers in random_list:
	sum = sum + 1
	print(sum) 
print(len(random_list))

student_score = []

sum = 0;
for _ in range(5):
	score = int(input("Enter score: "))
	student_score.append(score)
	sum = sum + 1
print("The length of the list is:", sum)



name = [1]
smallest = name[0]
print(smallest)
print(name)
'''