def sharepurchasecostanalyzer():
    try:
        company_name = input("Enter company name: ")
        number_of_shares = int(input("Enter number of shares purchased: "))
        share_price = float(input("Enter price per share (₹): "))
        brokerage_rate = float(input("Enter brokerage rate (%): "))
        other_charges = float(input("Enter additional charges (₹): "))

        if number_of_shares <= 0:
            print("Number of shares must be greater than zero.")
            return

        if share_price < 0 or brokerage_rate < 0 or other_charges < 0:
            print("Price and charges cannot be negative.")
            return

        purchase_value = number_of_shares * share_price
        brokerage = purchase_value * brokerage_rate / 100
        total_cost = purchase_value + brokerage + other_charges
        cost_per_share = total_cost / number_of_shares

        print("\nShare Purchase Cost Analysis")
        print("Company Name:", company_name)
        print("Number of Shares:", number_of_shares)
        print("Price Per Share: ₹", round(share_price, 2))
        print("Purchase Value: ₹", round(purchase_value, 2))
        print("Brokerage: ₹", round(brokerage, 2))
        print("Additional Charges: ₹", round(other_charges, 2))
        print("Total Purchase Cost: ₹", round(total_cost, 2))
        print("Actual Cost Per Share: ₹", round(cost_per_share, 2))

    except ValueError:
        print("Please enter valid numeric values.")

sharepurchasecostanalyzer()