def future_investment(investment_amount, monthly_interest_rate, years):
	return investment_amount * (1 + monthly_interest_rate)**years


investment_amount = int(input("Enter investment amount: "))
interest_rate = int(input("Enter monthly interst rate: "))
months = int(input("Enter number of months: "))
years = months/12
answer = (future_investment(investment_amount, interest_rate, years))
print("The future innvestment is", answer)