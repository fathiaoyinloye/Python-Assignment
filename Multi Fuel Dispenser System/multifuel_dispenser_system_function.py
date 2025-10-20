def home_menu():
	home_menu = """
*********************************************************
*	Welcome To OmoTemmy's Petroleum Station!!!	*
*********************************************************
*		1 	Buy Petroleum			*
*		2	Show Transaction History	*
*********************************************************
	"""
	return home_menu



def menu ():
	menu = """
*********************************************************
*		AVAILABLE PETROLEUM			*
*********************************************************
*	1	Petrol 		---->	350		*
*	2	Diesel		---->	400		*
*	3      Kerosene		---->	500 		*
*	4	Gas		---->	650		*
*********************************************************
	"""
	return menu

def calculate_total_cost(product, liter,price,transaction=[]):
	if (liter < 1 or liter > 50):
		return "Liters must be between 1 - 50"
	else:
		cost = liter * price
		receipt = f"""
*********************************************************
*	Customer's Transaction Receipt			*
*********************************************************
*	product 	---->	{product}		*
*	Amount		---->	{cost}			*
*	Liters		---->	{liter}L		*
*		Thank You for Your Patronage		*
*********************************************************
"""
		transaction.append(receipt)

		return receipt

def calculate_liters(product, cost,price,transaction=[]):
	if (cost < price):
		return "Amount must be above a liter price"
	else:
		liter = cost / price
		receipt = f"""
*********************************************************
*	Customer's Transaction Receipt			*
*********************************************************
*	product 	---->	{product}		*
*	Amount		---->	{cost}			*
*	Liters		---->	{liter}L		*
*		Thank You for Your Patronage		*
*********************************************************
"""
		transaction.append(receipt)
		return receipt

print(calculate_liters("Fuel",1200,7000))


def show_transactions(transactions):
	if transactions == []:
		return "No transaction made yet"
	else:

		for transaction in transactions:
			print(transaction)
		return "Thanks For Your Patronage"

