random_list = [1,2,3,4,5,6,7,8,9,10]

sum = 0;
for numbers in random_list:
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