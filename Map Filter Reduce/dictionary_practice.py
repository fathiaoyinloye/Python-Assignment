dictonary_list = {"1": "boy", "2": "girl", "3": "woman", "4" : "man"}

gender = input("Choose 1 - 4 to get what you are: ")

while(gender != "1" and gender != "2" and gender != "3" and gender != "4"):
	gender = input("Choose 1 - 4 to get what you are: ")
	if(gender == "1" or gender == "2" or gender == "3" or gender == "4"):
		break;

choice= input("Choose a thing: ")

dictonary_list[gender] = choice
print(dictonary_list[gender])

for key,value in dictonary_list.items():
	print(value)
del dictonary_list["1"]
print(dictonary_list)
print(dictonary_list.get("8", "Not found"))