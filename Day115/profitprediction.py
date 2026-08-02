def profitprediction():
    cost_price = float(input("Enter the cost price: "))
    expected_profit_percentage = float(input("Enter the expected profit percentage: "))

    expected_profit = (cost_price * expected_profit_percentage) / 100
    predicted_selling_price = cost_price + expected_profit

    print("Expected Profit:", round(expected_profit, 2))
    print("Predicted Selling Price:", round(predicted_selling_price, 2))

profitprediction()