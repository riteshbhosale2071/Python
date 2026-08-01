def discountvsprofit():
    marked_price = float(input("Enter the marked price: "))
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))

    discount = marked_price - selling_price
    discount_percentage = (discount / marked_price) * 100

    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100

    print("Discount Percentage:", round(discount_percentage, 2), "%")

    if profit >= 0:
        print("Profit Percentage:", round(profit_percentage, 2), "%")
    else:
        print("Loss Percentage:", round(abs(profit_percentage), 2), "%")

discountvsprofit()