def costprice():
    selling_price = float(input("Enter the selling price: "))
    profit_percentage = float(input("Enter the profit percentage: "))

    cost_price = selling_price / (1 + profit_percentage / 100)

    print("Cost Price:", round(cost_price, 2))

costprice()