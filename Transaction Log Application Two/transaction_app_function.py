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


def deposit(amount, account_balance,transactions=[]):
	if amount < 0:
		account_balance = account_balance
		account_balance = account_balance - 0
		result = "Transaction failed due to invalid input"
		transactions.append(result)
		print("Deposit failed: Invalid Amount")

	else: 
		account_balance += amount
		result = f"Deposited: N{amount}|| New Balance: {account_balance}"
		transactions.append(result)
	return account_balance
		
def withdraw(amount, account_balance,transactions=[]):
	if amount > account_balance:
		account_balance = account_balance - 0
		result = "Transaction failed due to insufficient balance"
		transactions.append(result)
		print("Withdrawal failed: Insufficient Fund")
		
	else:
		account_balance -= amount
		result = f"Withdraw: N{amount}|| New Balance: {account_balance}"
		transactions.append(result)

	return account_balance
def show_transactions(transactions):
	for transaction in transactions
		print transaction
	return "All Transaction"