def sellingpricefinder():
    cost_price = float(input("Enter the cost price: "))
    profit_percentage = float(input("Enter the profit percentage: "))

    profit = (cost_price * profit_percentage) / 100
    selling_price = cost_price + profit

    print("Profit Amount:", round(profit, 2))
    print("Selling Price:", round(selling_price, 2))

sellingpricefinder()