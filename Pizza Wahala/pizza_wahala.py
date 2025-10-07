from pizza_wahala_calculation import *


menu = """


			WELCOME TO IYA MOSES PIZA JOINT
	*********************************************************************************
		No	PIZZA TYPE	*   NUMBER OF SLICES	*	PRICE PER BOX	
	*********************************************************************************
		1	Sapa size	*	4		*		2,500	
	*********************************************************************************
		2	Small Money	*	6		*		2900	
	*********************************************************************************
		3	Big boys	*	8		*		4,000	
	*********************************************************************************
		4	Odogwu		*	12		*		5,200	
	*********************************************************************************
	
	


"""
print(menu)
menu_choice = input("Choose Pizza Type : ").lower() 


match menu_choice:
	case "sapa size" :
		people = int(input("Enter the number of people eating the Pizza: "))
		print (get_sapa_Size(people))

	case "small money" :
		people = int(input("Enter the number of people eating the Pizza: "))
		print (get_small_Size(people))


	case "big boys" :
		people = int(input("Enter the number of people eating the Pizza: "))	
		print (get_big_Size(people))

	case "odogwu" : 
		people = int(input("Enter the number of people eating the Pizza: "))
		print (get_odogwu_Size(people))

	case _ : print("Invalid Choice")
