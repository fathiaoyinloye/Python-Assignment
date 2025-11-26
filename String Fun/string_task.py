import random
def find_occurrence(myString, keyword):
    myString = myString.lower()
    myListOFString = myString.split()
    occurrence = 0
    for word in myListOFString:
        if keyword == word:
            occurrence += 1

    return occurrence

def find_last_index_of_occurrence(myString, keyword):
    myString = myString.lower()
    myListOFString = myString.split()
    my_list = []
    length = 0
    for word in myListOFString:
        length += len(word)
        if keyword == word:
            my_list.append(length)
        length += 1
    return my_list



def get_all_index_of_occurrence(myString,keyword):
    myList = find_last_index_of_occurrence(myString, keyword)
    new_list = []
    for number in myList:
        tuple = (number - len(keyword), number - 1)
        new_list.append(tuple)
    return new_list


def generate_random_string(pattern):
    my_uppercase_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    outcome = ""
    for character in pattern:
        if character.isalpha():
           outcome += random.choice(my_uppercase_letter)
        elif character == "#":
            outcome += str(random.randint(0, 10))
        elif character == "@":
            outcome += random.choice(my_uppercase_letter).lower()
        else:
            outcome += character
    return outcome

print(generate_random_string("AAA-###-@@"))


