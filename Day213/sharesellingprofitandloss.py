def sharesellingprofitandloss():
    try:
        company_name = input("Enter company name: ")
        shares = int(input("Enter number of shares sold: "))
        purchase_price = float(input("Enter purchase price per share (₹): "))
        selling_price = float(input("Enter selling price per share (₹): "))
        brokerage = float(input("Enter total brokerage charges (₹): "))
        other_charges = float(input("Enter additional charges (₹): "))

        if shares <= 0:
            print("Number of shares must be greater than zero.")
            return

        if min(purchase_price, selling_price, brokerage, other_charges) < 0:
            print("Prices and charges cannot be negative.")
            return

        purchase_value = shares * purchase_price
        selling_value = shares * selling_price

        total_cost = purchase_value + brokerage + other_charges
        net_profit_loss = selling_value - total_cost

        profit_loss_percentage = (net_profit_loss / total_cost) * 100 if total_cost > 0 else 0

        print("\nShare Selling Analysis")
        print("Company Name:", company_name)
        print("Number of Shares:", shares)
        print("Purchase Value: ₹", round(purchase_value, 2))
        print("Selling Value: ₹", round(selling_value, 2))
        print("Brokerage Charges: ₹", round(brokerage, 2))
        print("Additional Charges: ₹", round(other_charges, 2))
        print("Total Investment Cost: ₹", round(total_cost, 2))

        if net_profit_loss > 0:
            print("Net Profit: ₹", round(net_profit_loss, 2))
        elif net_profit_loss < 0:
            print("Net Loss: ₹", round(abs(net_profit_loss), 2))
        else:
            print("Result: No Profit, No Loss")

        print("Profit/Loss Percentage:", round(profit_loss_percentage, 2), "%")

    except ValueError:
        print("Please enter valid numeric values.")

sharesellingprofitandloss()