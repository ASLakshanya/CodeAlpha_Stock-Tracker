stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "AMAZON": 130,
    "MICROSOFT": 310
}

portfolio = {}
print("Welcome to the Stock Portfolio Tracker!")
print("You can buy these stocks:", list(stock_prices.keys()))
print("Type 'done' when you are finished.\n")

while True:
    stock_name = input("Enter stock name: ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("That stock is not available.")
        continue
    quantity = input("Enter quantity: ")
    if not quantity.isdigit():
        print("Please enter a valid number.")
        continue
    quantity = int(quantity)

    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

print("\nYour Portfolio:")
total = 0

for stock in portfolio:
    price = stock_prices[stock]
    qty = portfolio[stock]
    value = price * qty
    print(stock, ":", qty, "shares x $", price, "=", "$" + str(value))
    total += value
print("\nTotal Investment: $", total)

save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        for stock in portfolio:
            f.write(stock + ": " + str(portfolio[stock]) + " shares @ $" + str(stock_prices[stock]) + "\n")
        f.write("Total Investment: $" + str(total))
    print("Portfolio saved to 'portfolio.txt'")