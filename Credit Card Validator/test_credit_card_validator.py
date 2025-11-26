from credit_card_validator_functions import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_that_string_can_be_converted_to_an_array_of_numbers(self):
        expected = [1,2,3,4]
        actual = get_list_of_Numbers("1234")
        self.assertEqual(actual, expected)  # add assertion here

    def test_that_two_digits_number_can_be_sum_up(self ):
        actual = get_sum_of_digits_in_a_two_digit_number(12)
        self.assertEqual(actual, 3)

    def test_that_every_number_in_even_position_can_be_sum_up_from_right_to_left(self ):
        actual = get_sum_of_even_digits_from_right_to_left([1,2,3,4,5,7])
        expected = 9
        self.assertEqual(actual, expected)

    def test_that_every_number_in_odd_position_can_be_sum_up_from_right_to_left(self ):
        actual = get_sum_of_odd_digit_from_right_to_left([1,2,3,4,5])
        expected = 9
        self.assertEqual(actual, expected)

    def test_validity_of_a_card(self):
        actual = get_card_validity_status("5399831619690403")
        expected = "Valid"

    def test_status_of_a_card(self):
        actual = get_type_of_credit_card("5399831619690403")
        expected = "MasterCard"
        self.assertEqual(actual, expected)

