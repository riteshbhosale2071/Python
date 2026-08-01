def shopkeeperprofit():
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))

    profit = selling_price - cost_price

    if profit > 0:
        profit_percentage = (profit / cost_price) * 100
        print("Profit:", profit)
        print("Profit Percentage:", round(profit_percentage, 2), "%")
    elif profit < 0:
        print("Loss:", abs(profit))
    else:
        print("No Profit, No Loss")

shopkeeperprofit()