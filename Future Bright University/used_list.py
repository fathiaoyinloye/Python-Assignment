
university_record =  {}


def createAStudentRecord(name,age,courses,address,username):
	student_record = {}
	newDict ={"name" : None, "age": None, "courses" : None, "address" : None}
	newDict["name"] = name
	newDict["age"] = age
	newDict["courses"] = courses
	newDict["address"] = address
	university_record[username] = newDict
	return "Student record have been successfully created."



def display_student_record(username):
	if len(university_record) == 0:
			print("No student have been registered yet")
	for records in university_record:
		for key,value in records.items():
			if username == key:
				key_index = university_record.index(records)
				for key,value in university_record[key_index][username].items():
					if type(value) == dict:
						for keys,val in value.items():
							print(f"{keys} => {val}")
					elif type(value) == list:
						print(f">>>{key}<<<")
						for course in value:
							print(course)

					else: 
						print(f"{key} => {value}")
	
def display_student_course(username):	
	if len(university_record) == 0:
			print("No student have been registered yet")
	for records in university_record:
		for key,value in records.items():
			if username == key:
				key_index = university_record.index(records)
				for key,value in university_record[key_index][username].items():
					if type(value) == list:
						print(f">>>{key}<<<")
						for course in value:
							print(course)




def menu():
	show_menu = """
***************************************************
Welcome To Future Bright University Application
***************************************************
>>>>>>>>>>>>>>>>Choose From Option Below<<<<<<<<<<<
1 	=>	Register a student
2	=> 	Display a student record
3	=> 	Display a student course
4	=>	Exit application
*****************************************************
"""
	return show_menu





















