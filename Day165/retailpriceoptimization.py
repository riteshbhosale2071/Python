def retailpriceoptimization():
    print("Retail Price Optimization Program :")

    cost_price = float(input("Enter the cost price: "))
    discount_percentage = float(input("Enter the expected discount percentage: "))
    desired_profit_percentage = float(input("Enter the desired profit percentage: "))

    if cost_price > 0 and 0 <= discount_percentage < 100 and desired_profit_percentage >= 0:
        required_selling_price = cost_price + (cost_price * desired_profit_percentage / 100)

        marked_price = required_selling_price / (1 - discount_percentage / 100)

        discount_amount = marked_price * discount_percentage / 100
        profit_amount = required_selling_price - cost_price

        print("Recommended Marked Price:", round(marked_price, 2))
        print("Discount Amount:", round(discount_amount, 2))
        print("Final Selling Price:", round(required_selling_price, 2))
        print("Expected Profit:", round(profit_amount, 2))
        print("Expected Profit Percentage:", desired_profit_percentage, "%")
    else:
        print("Enter valid cost, discount, and profit values.")

retailpriceoptimization()