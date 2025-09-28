total_miles_driven = 0
count = 0
total_gallons_used = 0
while(count != -1):

	miles_driven = float(input("Enter the  miles driven: "))
	total_miles_driven = total_miles_driven + miles_driven

	gallons_used = float(input("Enter the gallon used: "))
	total_gallons_used = total_gallons_used + gallons_used 


	miles_per_gallons = miles_driven/gallons_used
	print("The miles per gallon is", miles_per_gallons)

	count = int(input("Enter -1 to end or any number to continue: "))

total_average = total_miles_driven/ total_gallons_used

print("The total miles per gallon of all your trips is", total_average )
