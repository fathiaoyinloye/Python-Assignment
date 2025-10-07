def get_sapa_Size(people):
	boxes = people//4
	if(people % 4 != 0):
		boxes = boxes + 1
				
	total_slice = 4 * boxes
	remainder = total_slice - people
	price = boxes * 2500
		
			
	print("The number of boxes slice is: ", boxes)
	print("The number of remaining slice is: ", remainder)
	print("The prices of Pizza is: ", price)


def get_small_Size(people):
	boxes = people//6
	if(people % 6 != 0):
		boxes = boxes + 1
				
	total_slice = 6 * boxes
	remainder = total_slice - people
	price = boxes * 2900
		
			
	print("The number of boxes slice is: ", boxes)
	print("The number of remaining slice is: ", remainder)
	print("The prices of Pizza is: ", price)

def get_big_Size(people):
	boxes = people//8
	if(people % 8 != 0):
		boxes = boxes + 1
				
	total_slice = 8 * boxes
	remainder = total_slice - people
	price = boxes * 4000		
			
	print("The number of boxes slice is: ", boxes)
	print("The number of remaining slice is: ", remainder)
	print("The prices of Pizza is: ", price)

def get_odogwu_Size(people):
	boxes = people//12
	if(people % 12 != 0):
		boxes = boxes + 1
				
	total_slice = 12 * boxes
	remainder = total_slice - people
	price = boxes * 5200
		
			
	print("The number of boxes slice is: ", boxes)
	print("The number of remaining slice is: ", remainder)
	print("The prices of Pizza is: ", price)

print (get_sapa_Size(15))
print (get_small_Size(15))
print (get_big_Size(15))
print (get_odogwu_Size(15))