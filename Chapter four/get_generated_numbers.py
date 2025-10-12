import random

def generate_number():
	number1 = random.randrange(0,9)
	number2 = random.randrange(0,9)
	return (number1, number2)

def generate_correct_response():
	random_correct_response = random.randrange(1,4)
	if random_correct_response  == 1:
		response = "Very Good!"

	if random_correct_response  == 2:
		response = "Nice Work!"
	if random_correct_response  == 3:
		response = "Keep up the Good Work!"
	return response


def generate_incorrect_response():
	random_incorrect_response = random.randrange(1,4)
	if random_incorrect_response  == 1:
		response = "No. Please try again."

	if random_incorrect_response  == 2:
		response = "Wrong.Try once more."
	if random_incorrect_response  == 3:
		response = "No. Keep trying."
	return response


def generate_number_two():
	number1 = random.randrange(10,100)
	number2 = random.randrange(10,100)
	return (number1, number2)

def print_options():

	options ="""
*********************************************************
*	Welcome Victorious Jewel!!!			*
*	Let  Solve Arithmetic Problem			*
*	Your Writing Material With You			*
*	Get Ready For An Amazing Experince		*
*	Bring Out The Genius in You			*
*********************************************************


*********************************************************
*	Choose Arithmetic Operation Of Your Choice	*
*********************************************************
*		No	Arithmetic Operation		*
*		1 		Addition		*
*		2		Subtraction		*
*		3		Multiplication		*
*		4		Division		*
*********************************************************
	"""
	return options

def choose_level():
	level = """
*********************************************************
*	Choose The Level Of Your Choice			*
*********************************************************
*		No		Level			*
*		1 		Easy			*
*		2		Difficult		*
*********************************************************
	"""
	return level

