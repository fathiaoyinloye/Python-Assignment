'''
	prompt user to enter father's age 
	collect father's  name from user assign it to a vraible fatherage
	prompt user to enter son's age
	collect son's  name from user  assign it to a variable sonage
	calculate twice the son age by multiplying the age by 2 and assign the result to variable twicesonage
	deduct twice the son age from the current father's age to get how many  years ago was he twice his son's age
	print the age the father was when he was twice his son's age
'''


FATHERAGE = int(input("Enter current father's age: "))
SONAGE = int(input("Enter current son's age: "))
twice_son_age = SONAGE * 2
father_twice_son_age = FATHERAGE - twice_son_age
print("The father was twice his son's age " , father_twice_son_age, "years ago.");
	
