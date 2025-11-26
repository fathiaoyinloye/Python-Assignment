def get_list_of_Numbers(credit_number):
    my_list = []
    for character in credit_number:
        my_list.append(int(character))
    return my_list


def getDoubleNumber(number):
    return number * 2

def get_sum_of_digits_in_a_two_digit_number(number):
    return number - 9

def get_sum_of_even_digits_from_right_to_left(numbers):
    sum = 0
    for number in range (len(numbers)-2, -1, -2):
        doubledNumber = getDoubleNumber(numbers[number])
        if(doubledNumber > 9):
            doubledNumber = get_sum_of_digits_in_a_two_digit_number(doubledNumber)
        sum += doubledNumber
    return sum

def get_sum_of_odd_digit_from_right_to_left(numbers):
    sum = 0
    for number in range (len(numbers)-1, -1, -2):
        sum += numbers[number]
    return sum

def get_card_validity_status(credit_number):
    my_list = get_list_of_Numbers(credit_number)
    numberOne = get_sum_of_odd_digit_from_right_to_left(my_list)
    numberTwo = get_sum_of_even_digits_from_right_to_left(my_list)
    sum = numberOne + numberTwo
    if sum % 10 == 0:
        return "Valid"
    else:
        return "Invalid"

def get_type_of_credit_card(credit_number):
    my_list = get_list_of_Numbers(credit_number)
    if len(my_list) < 13 or len(my_list) > 16:
        return "Invalid"
    elif my_list[0] == 4:
        return "Visa Cards"
    elif my_list[0] == 5:
        return "MasterCard"
    elif my_list[0] == 6:
        return "Discover Cards"
    elif my_list[0] * 10 + my_list[1] == 37:
        return "American Express Cards"



