# 	promt user to enter age
#	maximum heart rate is subtracting age from 220
#	range calculated by multiplying 50 and 85% to the maximum heart rate
#	print maximum heartbeat and range
age = int (input("Enter your age: "))

maximum_heart_rate = 220 - age

print("Your maximum heart rate is", maximum_heart_rate, "bpm")

lower_range = 50/100 * maximum_heart_rate 
upper_range = 85/100 * maximum_heart_rate 

print("Range of your target heart rate falls between", lower_range, "bpm to", upper_range, "bpm")
