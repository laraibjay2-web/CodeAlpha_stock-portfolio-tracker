stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 150,
    "MSFT" : 400,
    "AMZN" : 190,
}

portfolio = []

print("============================")
print("     STOCK PORTFOLIO TRACKER       ")
print("============================")


print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":" , "$", price)


total_stocks = int(input("\nHow many different stocks do you want to buy? "))

for i in range(total_stocks):

    print("\nStock", i + 1)

    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater then zero.")
            continue

        price = stock_prices[stock_name]

        investment = price * quantity

        portfolio.append({
            "stock": stock_name,
            "price": price,
            "quantity": quantity,
            "investment": investment
        })

        print("Investment added successfully!")

    else:
        print("Stock not available! Please choose from the list.")

total_investment = sum(
    item["investment"] for item in portfolio
)

print("\n===========================")
print("        YOUR STOCK PORTFOLIO            ")
print("===============================")



for item in portfolio:
    print("\nStock:", item["stock"])
    print("Price per share: $", item["price"])
    print("Quantity:" , item["quantity"])
    print("Total investment: $", item["investment"])

print("\n==============================")
print("Total Investment: $", total_investment)
print("=================================")


with open("portfolio.txt", "w") as file:

    file.write("STOCK PORFOLIO REPORT\n")
    file.write("======================\n")

    for item in portfolio:
        file.write(
            f"\nStock: {item["stock"]}\n"
            f"Price: ${item["price"]}\n"
            f"Quantity: {item["quantity"]}\n"
            f"Investment: ${item["investment"]}\n"
        )

    file.write(
        f"\n Total Investment: ${total_investment}\n"
    )

print("\nYour portfolio has been saved in portfolio.txt")
