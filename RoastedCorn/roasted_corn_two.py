import random
def create_a_new_list():
    my_list = []
    for number in range(0, 10):
        my_random_number = random.randint(1, 51)
        my_list.append(my_random_number)
    return my_list

def get_length_of_list(my_list):
    count = 0
    for _ in my_list:
        count+= 1
    return count

def sum_up_elements_at_even_position(my_list):
    sum_of_list = 0
    for index in range(0, len(my_list), 2):
        sum_of_list += my_list[index]
    return sum_of_list


def sum_up_elements_at_odd_position(my_list):
    sum_of_list = 0
    for index in range(1, len(my_list), 2):
        sum_of_list += my_list[index]
    return sum_of_list

def multiply_elements_at_third_position(my_list):
    multiples = 1
    for index in range(3, len(my_list), 3):
        multiples *= my_list[index]
    return multiples

def calculate_sum(my_list):
    sum_of_my_list = 0
    for number in my_list:
        sum_of_my_list  += number
    return sum_of_my_list

def calculate_average(my_list):
    my_sum = calculate_sum(my_list)
    average = my_sum/len(my_list)
    return average

def calculate_highest(my_list):
    highest = 0
    for number in my_list:
        if number > highest:
            highest = number
    return highest

def calculate_lowest(my_list):
    lowest = my_list[0]
    for number in my_list:
        if number < lowest:
            lowest = number
    return lowest

def count_number_of_strings_in_a_list(my_list):
    new_list = []
    for characters in my_list:
        if len(characters)  >= 2:
            if(characters[0] == characters[-1]):
                new_list.append(characters)
    return new_list

def create_a_sorted_list_ranging_from_one_to_fifteen():
    my_list = []
    for number in range(0, 10):
        my_random_number = random.randint(1, 16)
        my_list.append(my_random_number)
        my_list.sort()
    return my_list

def duplicate_numbers_in_a_list():
    my_list = create_a_sorted_list_ranging_from_one_to_fifteen()
    new_list = []
    for number in my_list:
        new_list.append(number)
        new_list.append(number)
    new_list.sort()
    return new_list

def eleminate_duplicate_numbers_in_a_list():
    my_list = duplicate_numbers_in_a_list()
    new_list = []
    for number in my_list:
        if number not in new_list:
            new_list.append(number)
    return new_list

def sum_up_every_third_elements_in_a_list(my_list ):
    sum_third_elements = 0
    for number in range(0, len(my_list), 3 ):
       sum_third_elements += my_list[number]
    return sum_third_elements

def calculate_sum_of_first_middle_and_last_element_in_a_list(my_list):
    total = my_list[0]+my_list[-1]+ my_list[(len(my_list)// 2 )]
    if len(my_list) % 2 == 0:
        average = (my_list[len(my_list)//2 - 1] + my_list[len(my_list)//2])/ 2
        total = my_list[0] + my_list[-1] + average
    return total

def collect_ten_numbers_from_users_without_showing_duplicates():
    my_set = set()
    for number in range(10):
        number = int(input("Enter a number: "))
        my_set.add(number)
    return my_set

def remove_item(my_set, number):
    if number in my_set:
        my_set.remove(number)
        return number
    else:
        return None

def find_intersection(first_set, second_set):
    new_set = first_set.intersection(second_set)
    return new_set

def find_union(first_set, second_set):
        new_set = first_set.union(second_set)
        return new_set



def check_subset(first_set, second_set):
    return first_set.issubset(second_set)


def remove_elements(first_set):
    first_set.clear()
    return first_set

def find_minimum_and_maximum_number(second_set):
    if len(second_set) == 0:
        return "Inputed set is empty"

    my_list = list(second_set)
    maximum = my_list[0]
    minimum = my_list[0]
    for number in my_list:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return maximum, minimum


def check_length_of_set(my_set):
    my_list = list(my_set)
    count = 0
    for number in my_list:
        count += 1

    return count

def create_a_list():
    my_list = []
    for number in range(0, 10):
        my_random_number = random.randint(1, 21)
        my_list.append(my_random_number)
    return my_list

def create_a_tuple():
    my_tuple = ()
    return my_tuple

my_tuple = create_a_list()
my_tuple = tuple(create_a_list())
sum_of_tuple_odd_position = sum_up_elements_at_odd_position(list(my_tuple))
sum_of_tuple_even_position = sum_up_elements_at_even_position(list(my_tuple))
first,second,third,fourth,fifth, *rest = my_tuple



my_dict = {}

for number in range(1, 3):
    name = input(f"Enter name of student{number}: ")
    age = input(f"Enter{name}'s age: ")
    my_dict[name] = age




sum_of_age = 0
for key, value in my_dict.items():
    sum_of_age += value

print(sum_of_age)






