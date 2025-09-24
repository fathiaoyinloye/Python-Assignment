"""	prompt user to enter  scores for three student
	collect the scores and assign  it to their variable
	average should be calculated as total of all grade divided by 3
	if score is greater than and equal to 90, print A, if not
	if score is greater than and equal to 80, print B, if not
	if score is greater than and equal t0 60, print C, if not
	if score is less than 60, print F.
"""


SCORE1 = int (input("Enter student score: " ))		
SCORE2 = int (input("Enter student score: " ))	
SCORE3 = int (input("Enter student score: " ))		
	
average = (SCORE1  + SCORE2 + SCORE3) / 3
print(f"The scores average is {average: .2f}")

if(SCORE1 >= 90):
	print("A")
		

elif(SCORE1 >= 80):
	print("B")
		
elif(SCORE1 >= 70):
	print("C")

elif(SCORE1 >= 60):  
	print("D")
		
else:
	print("F")

if(SCORE2 >= 90):
	print("A")
		

elif(SCORE2 >= 80):
	print("B")
		
elif(SCORE2 >= 70):
	print("C")

elif(SCORE2 >= 60):
	print("D")
		
else:
	print("F")
		

if(SCORE3 >= 90):
	print("A")
		

elif(SCORE3 >= 80):
	print("B")
		
elif(SCORE3 >= 70):
	print("C")

elif(SCORE3 >= 60):
	print("D")
		
else:
	print("F")



	
