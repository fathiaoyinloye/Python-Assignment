# data = input("Enter student record: ")
#
# first_name, last_name = data.split()

def save_student_records(first_name, last_name):
        with open("users.txt", "a") as file:
            record = {"first_name": first_name, "last_name": last_name}
            file.write(f"{record}\n")


def read_student_record(first_name, last_name):
    with open("users.txt", "r") as file:
        for record in file.readlines():
            for key,value in record.items():
             print(value)
         # return record.keys() == first_name and last_name == last_name
    return False
#
# count = 3
# while count > 0:
#     first = input("What is your first name? ")
#     last = input("What is your last name? ")
#     save_student_records(first,last )
#     count -= 1
read_student_record("Oyinloye", "Fathia")

