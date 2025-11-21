from bright_university_function import *
my_subject = {"math", "physics", "computer science", "biology", "chemistry", "statistics", "english", "economics", "history", "philosophy", "sociology", "political science", "geography", "psychology", "art", "music", "engineering", "law", "medicine", "business"}
while True:
	print(menu())
	option = input("Choose from option above: ")
	match(option):
		case "1":				
			courses_offerred = []
	
			name = input("Enter student name: ")
			age = input(f"Enter {name} age: ")
			while age.isdigit() == False:
				print("Invalid age, please enter student age: ")
				age = input(f"Enter {name} age: ")
			going = True
			while(going):
				no_of_course = input(f"Enter number of course {name} wants to register: ")
				while no_of_course.isdigit() == False:
					print(f"Invalid Number of course, please enter the number of course {name} is to  offer: ")
					no_of_course = input(f"Enter number of course {name} wants to register: ")
				no_of_course = int(no_of_course)
				if(no_of_course > len(my_subject) or no_of_course  < 1 ):
					print("No of courses to be offerred cannot be less than 1 or greater than courses offerred in the college.")
				else:
					break
			while(no_of_course > 0):
				course = input("Enter the course to be registered: ").lower()
				if course in my_subject and course not in courses_offerred:
					courses_offerred.append(course)	
				else: 
					print("Invalid Input, Course Inputed is not offerred in the collede")
					no_of_course += 1
	
				no_of_course -= 1
			address = {}
			city = input("Enter student city: ")
			zipcode = input(f"Enter {city} zipcode: ")
			username = input("Enter student username:")
			address["city"] = city
			address["zipcode"] = zipcode
			print(createAStudentRecord(name,age,courses_offerred,address,username))
		case "2":
			username = input("Enter student username to display student record: ")
			display_student_record(username)
		case "3":
			username = input("Enter student username to display courses registered: ")
			response = display_student_course(username)
			if type(response) == tuple:
				print(f"<<<<{response[0]}>>>>")
				for course in response[1]:
					print(course)
			else:
				print(response)
		case "4":
			username = input("Enter student username to display student address zipcode: ")
			response = display_zip_code(username)
			if type(response) == tuple:
				for item in response:
					print(item)

			else:
				print(response)
		case "5":
			username = input("Enter student username to display student address zipcode: ")
			response = display_city(username)
			if type(response) == tuple:
				for item in response:
					print(item)

			else:
				print(response)

		case "6":
			username = input("Enter student username to  add new Course: ")
			new_course = input("Enter new course to be added: ").lower()
			print(add_new_course(username, new_course, my_subject))

		case "7":
			username = input("Enter student username to  remove from existing course: ")
			course_to_remove = input("Enter new course to be remove from existing course: ").lower()
			print(remove_course(username, course_to_remove))

		case "8":
			username = input("Enter student username to  add new Course: ")
			course_to_update = input("Enter old course to be updated: ").lower()
			new_course = input("Enter new course to be to replace old course offered: ").lower()
			print(update_course(username, new_course, my_subject,course_to_update))


		case "9":
			field = input("Enter field to be changed: ").lower()
			username = input("Enter student username to  change field: ")
			before = input(f"Enter old {field} to be updated: ").lower()
			after = input(f"Enter new {field} to be replace old  one: ").lower()
			print( update_student_field(username, field, before,after))

		case "10":
			print(display_the_overall_number_of_student())

		case "11":
			print("Exiting application...")
			break;

		case _ : print("Invalid Input")

	
