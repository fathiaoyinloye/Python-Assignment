def my_discount (price, discount):
	discount = price * discount/100
	return price - discount

price = int (input("Enter the price: "))
discount = int(input("Enter discount given: "))

print("The price after discount is", (my_discount(price, discount)))