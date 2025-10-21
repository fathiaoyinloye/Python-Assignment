def calculate_liter(product, amount):
	if product == "1" and amount < 1000:
		return "Amount must be greater than a litre's price"
	elif product == "1" and amount > 1000:

		return amount/1000

	if product == "2" and amount < 500:
		return "Amount must be greater than a litre's price"
	elif product == "2" and amount > 500:

		return amount/500

	if product == "3" and amount < 1500:
		return "Amount must be greater than a litre's price"
	elif product == "3" and amount > 1500:

		return amount/1500

	if product == "4" and amount < 700:
		return "Amount must be greater than a litre's price"

	elif product == "4" and amount > 700:

		return amount/700

def calculate_cost(product, liter):
	if product == "1" and liter < 1 or liter > 50:
		return "Liters must be between 1 - 50"

	elif product == "1" and liter >= 1 and liter  <= 51:

		return 1000 * liter

	if product == "2" and liter < 1 or liter > 50:
		return "Liters must be between 1 - 50"

	elif product == "2" and liter >= 1 and liter  <= 50:

		return 500 * liter


	if product == "3" and liter < 1 or liter > 50:
		return "Liters must be between 1 - 50"

	elif product == "3" and liter >= 1 and liter  <= 50:

		return 1500 * liter

	if product == "4" and liter < 1 or liter > 50:
		return "Liters must be between 1 - 50"

	elif product == "4" and liter >= 1 and liter <= 50:

		return 700 * liter


def show_receipts(product,cost):
	liter = calculate_liter(product, cost)
	if type(liter) in [int, float]:
		return f"""
*********************************************************
	Customer's Transaction Receipt			
*********************************************************
	product 	---->	{product}		
	Amount		---->	{cost}			
	Liters		---->	{liter}L		
		Thank You for Your Patronage		
*********************************************************
"""
	return ""


def show_transactions():
	...


print(show_receipts("1", 5000))


