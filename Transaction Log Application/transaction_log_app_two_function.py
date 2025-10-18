transactions = []
def deposit (amount, account_balance,transactions):
	
	account_balance = account_balance + amount
	transactions.append(f"Deposited {amount} and New Balance is {account_balance}")
	return account_balance
	
