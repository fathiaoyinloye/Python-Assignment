my_list = {"2211": {"name": "fathia", "class": "34"}, "567": {"name": "tope", "class": "67","courses": ["maths","English","Computer"], "address": {"city": "lagos", "zip": "896"}}}
result = my_list.get("567", "key not found")
myCourse = "maths","English","biology" 
result = my_list["567"]["courses"]
new_course = "biology"
if new_course not in result and new_course in myCourse:
	my_list["567"]["courses"].append(new_course)
	
print(my_list["567"]["courses"])