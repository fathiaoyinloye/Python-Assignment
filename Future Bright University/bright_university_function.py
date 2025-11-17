
university_record =  {}


def createAStudentRecord(name,age,courses,address,username):
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
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			print(response)
		else:
			for key,value in response.items():
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
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response
		else:
			
			for key,value in response.items():
				if type(value) == list:
					return key,value


def display_zip_code(username):
	if len(university_record) == 0:
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response

		else:
			zipcode = university_record[username]["address"]["zipcode"]
			return "<<<Zipcode>>>",zipcode

def display_city(username):
	if len(university_record) == 0:
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response

		else:
			city = university_record[username]["address"]["city"]
			return "<<<City>>>",city


def add_new_course(username, new_course, university_courses):
	if len(university_record) == 0:
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response

		else:
			result = university_record[username]["courses"]
			name = university_record[username]["name"]

			if new_course not in result and new_course in university_courses:
				university_record[username]["courses"].append(new_course)
				return f"{new_course} have been successfully added to courses offerred by {name}."
			elif new_course  in result:
				return f"Course already offerred by {name} cannot be offerred again"
			else:
				return f"Only courses approved by the College can be added"


def remove_course(username, course_to_remove):
	if len(university_record) == 0:
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response

		else:
			result = university_record[username]["courses"]
			name = university_record[username]["name"]
			if len(result) < 2:
				return f"{name} must offer at least one course"

			elif course_to_remove  in result:
				university_record[username]["courses"].remove(course_to_remove)
				return f"{course_to_remove} have been successfully removed from list of courses offerred by {name}."
			else:
				return f"Only courses already offerred by {name} can be remove"

def update_course(username, new_course, university_courses,course_to_update):
	if len(university_record) == 0:
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response

		else:
			result = university_record[username]["courses"]
			name = university_record[username]["name"]
			if course_to_update not in result:
				return f"Only course  in {name} offerred course can be updated"
			elif new_course not in university_courses:
				return "Only course the university approved can be  offerred"


			elif new_course  in result:
				return f"Course already offerred by {name} cannot be offerred twice"
			else:
				university_record[username]["courses"].remove(course_to_update)
				university_record[username]["courses"].append(new_course)
				return f"{course_to_update} have been successfully updated to {new_course} in courses offerred by {name}."	




def update_student_field(username, field, before,after):
	if len(university_record) == 0:
			return "No student have been registered yet"
	else:
		response = university_record.get(username,"Username not found")
		if response == "Username not found":
			return response

		elif field == "name":
			name = university_record[username]["name"]
			if before  != name:
				return f"Incorrect name inputed"
			else:
				university_record[username]["name"] = after
		
		elif field == "city":
			city = university_record[username]["city"]
			if before  != city:
				return f"Incorrect city inputed"
			else:
				university_record[username]["city"] = after
				return f"{before} have been successfully updated to {after} ."
		elif field == "age":
			age = university_record[username]["age"]
			if before  != age:
				return f"Incorrect age inputed"
			elif after.isdigit == False:
				return f"Incorrect age inputed, age should be in digits."

			elif int(after) < int(before):
				return f"You can only increase in age not decrease"
			else:
				university_record[username]["age"] = after
				return f"{before} have been successfully updated to {after} ."

		
		elif field == "zipcode":
			zipcode = university_record[username]["zipcode"]
			if before  != zipcode:
				return f"Incorrect zipcode inputed"
			else:
				university_record[username]["zipcode"] = after
				return f"{before} have been successfully updated to {after} ."
		else:
			return "Incorrect feild inputed"


			
def display_the_overall_number_of_student():
		return f"The overall number of student registered in the university system is {len(university_record)}"

def menu():
	show_menu = """
*****************************************************************************
Welcome To Future Bright University Application
*****************************************************************************
>>>>>>>>>>>>>>>>>>>>>>>>>>Choose From Options Below<<<<<<<<<<<<<<<<<<<<<<<<<
1 	=>	Register a student
2	=> 	Display a student record
3	=> 	Display a student course
4	=>	Display a student address zipcode
5	=>	Display a student address city
6	=>	Add a new course
7	=>	Remove an existing course
8	=>	Update an existing course
9	=>	Update student data(name,city,age,Zipcode)
10	=>	Display the number of student registered in the system
11	=>	Exit application


*****************************************************************************
"""
	return show_menu





















