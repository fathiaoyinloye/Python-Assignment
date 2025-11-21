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


print()