def shareinvestmentcalculator():
    try:
        company_name = input("Enter company name: ")
        shares = int(input("Enter number of shares purchased: "))
        purchase_price = float(input("Enter purchase price per share (₹): "))
        current_price = float(input("Enter current market price per share (₹): "))

        if shares <= 0 or purchase_price < 0 or current_price < 0:
            print("Please enter valid investment details.")
            return

        investment_amount = shares * purchase_price
        current_value = shares * current_price
        profit_loss = current_value - investment_amount

        if investment_amount > 0:
            return_percentage = (profit_loss / investment_amount) * 100
        else:
            return_percentage = 0

        print("\nShare Investment Analysis")
        print("Company Name:", company_name)
        print("Number of Shares:", shares)
        print("Purchase Price: ₹", round(purchase_price, 2))
        print("Current Price: ₹", round(current_price, 2))
        print("Total Investment: ₹", round(investment_amount, 2))
        print("Current Market Value: ₹", round(current_value, 2))

        if profit_loss > 0:
            print("Profit: ₹", round(profit_loss, 2))
        elif profit_loss < 0:
            print("Loss: ₹", round(abs(profit_loss), 2))
        else:
            print("No Profit or Loss.")

        print("Return Percentage:", round(return_percentage, 2), "%")

    except ValueError:
        print("Please enter valid numeric values.")

shareinvestmentcalculator()