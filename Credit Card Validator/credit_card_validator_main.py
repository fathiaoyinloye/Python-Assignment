from credit_card_validator_functions import *
card_number = input("Enter your credit card number: ")
print("Credit Card type: ", get_type_of_credit_card(card_number))
print("Credit Card number: ", card_number)
print("Credit Card digit length is ",  len(card_number))
print("Credit card Validity Status: ", get_card_validity_status(card_number))
