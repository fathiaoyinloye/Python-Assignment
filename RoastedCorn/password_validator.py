def password_validator(password):
        password_in_uppercase = password.upper()
        password_in_lowercase = password.lower()
        all_my_symbols = "`~!@#$%^&*()-_ +<>={[}]|\"\\:;',./?"
        number_for_upper = 0
        number_for_lower = 0
        number_for_symbol = 0
        number_for_length = 0
        number_for_digit = 0

        for character in password:
            if character in password_in_uppercase:
               number_for_upper = 1
            if character in password_in_lowercase:
                number_for_lower = 1

            if character in all_my_symbols:
                number_for_symbol = 1
            if character.isdigit():
                number_for_digit = 1
        if len(password) >= 10:
                number_for_length = 1

        number = number_for_upper +  number_for_lower + number_for_symbol + number_for_digit + number_for_symbol
        if number == 5:
            return"Strong"
        elif(number_for_upper == 1 and number_for_lower == 1 and number_for_symbol == 1):
                return "medium"
        else:
           return "Weak Pass"


password = input("Enter your password: ")
print(password_validator(password))