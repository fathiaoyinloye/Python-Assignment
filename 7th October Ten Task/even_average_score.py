sum = 0
for count in range(1, 11):
	score = int( input("Enter score: "))
	if(score % 2 == 0):
		sum += score
		count += 1
average =sum/count
print("The sum of even number is:", sum)  
print("The average of even number is:", average)  


