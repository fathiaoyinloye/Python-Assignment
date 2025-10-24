dictonary_list = {"1": "boy", "2": "girl", "3": "woman", "4" : "man"}

gender = input("Choose 1 - 4 to get what you are: ")

while(gender!= "1" or gender!= "2" or gender!= "3" or gender!= "4"):
	gender = input("Choose 1 - 4 to get what you are: ")
	if(gender == "1" or gender == "2" or gender == "3" or gender == "4"):
		break;
print(dictonary_list[gender])
