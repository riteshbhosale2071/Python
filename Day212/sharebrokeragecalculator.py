def sharebrokeragecalculator():
    try:
        company_name = input("Enter company name: ")
        shares = int(input("Enter number of shares: "))
        buy_price = float(input("Enter buying price per share (₹): "))
        sell_price = float(input("Enter selling price per share (₹): "))
        brokerage_rate = float(input("Enter brokerage rate (%): "))

        if shares <= 0 or buy_price < 0 or sell_price < 0 or brokerage_rate < 0:
            print("Please enter valid investment details.")
            return

        buy_value = shares * buy_price
        sell_value = shares * sell_price

        buy_brokerage = buy_value * brokerage_rate / 100
        sell_brokerage = sell_value * brokerage_rate / 100

        total_brokerage = buy_brokerage + sell_brokerage
        total_investment = buy_value + buy_brokerage
        net_sale_amount = sell_value - sell_brokerage

        profit_loss = net_sale_amount - total_investment

        print("\nShare Brokerage Report")
        print("Company Name:", company_name)
        print("Number of Shares:", shares)
        print("Buying Value: ₹", round(buy_value, 2))
        print("Selling Value: ₹", round(sell_value, 2))
        print("Buying Brokerage: ₹", round(buy_brokerage, 2))
        print("Selling Brokerage: ₹", round(sell_brokerage, 2))
        print("Total Brokerage: ₹", round(total_brokerage, 2))
        print("Total Buying Cost: ₹", round(total_investment, 2))
        print("Net Selling Amount: ₹", round(net_sale_amount, 2))

        if profit_loss > 0:
            print("Net Profit: ₹", round(profit_loss, 2))
        elif profit_loss < 0:
            print("Net Loss: ₹", round(abs(profit_loss), 2))
        else:
            print("No Profit or Loss.")

    except ValueError:
        print("Please enter valid numeric values.")

sharebrokeragecalculator()