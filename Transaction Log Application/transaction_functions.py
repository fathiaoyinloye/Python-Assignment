
def show_menu ():
	menu = """
*********************************************************
*	Welcome To Transaction Log Application		*
*********************************************************
*    Click any of the following to perform operation 	*
*		1 		Deposit			*
*		2		Withdraw		*
*		3		Show transactions	*
*		4		Exit			*
*********************************************************
	"""
	return menu


def get_deposit (amount, account_balance):
	#account_balance = account_balance + amount
	transaction = f"Deposited {amount} and New Balance is {account_balance}"
	
	return transaction
	
def withdraw(amount, account_balance):
	if(account_balance < amount):
		account_balance = account_balance - 0
		return "Withdrawal failed: Insufficient Fund"
		
	else:
		account_balance = account_balance - amount
		transaction = f"Withdrew {amount} and New Balance is {account_balance}"
	
		return transaction
		