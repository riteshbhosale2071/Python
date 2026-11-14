def sipinvestmentplanner():
    try:
        investor_name = input("Enter investor name: ")
        monthly_investment = float(input("Enter monthly SIP amount (₹): "))
        annual_return = float(input("Enter expected annual return (%): "))
        years = int(input("Enter investment period (years): "))
        annual_increase = float(input("Enter yearly SIP increase (%): "))

        if monthly_investment <= 0 or annual_return < 0 or years <= 0 or annual_increase < 0:
            print("Please enter valid investment details.")
            return

        monthly_rate = annual_return / (12 * 100)
        total_investment = 0
        future_value = 0
        current_sip = monthly_investment

        for year in range(years):
            for month in range(12):
                total_investment += current_sip

                if monthly_rate == 0:
                    future_value += current_sip
                else:
                    future_value = (
                        future_value * (1 + monthly_rate) + current_sip
                    )

            current_sip += current_sip * annual_increase / 100

        estimated_profit = future_value - total_investment
        return_percentage = (estimated_profit / total_investment) * 100

        print("\nSIP Investment Plan")
        print("Investor Name:", investor_name)
        print("Initial Monthly SIP: ₹", round(monthly_investment, 2))
        print("Expected Annual Return:", annual_return, "%")
        print("Yearly SIP Increase:", annual_increase, "%")
        print("Investment Period:", years, "years")
        print("Total Invested Amount: ₹", round(total_investment, 2))
        print("Estimated Profit: ₹", round(estimated_profit, 2))
        print("Estimated Future Value: ₹", round(future_value, 2))
        print("Estimated Return:", round(return_percentage, 2), "%")

        print("\nNote: Returns are estimates and are not guaranteed.")

    except ValueError:
        print("Please enter valid numeric values.")

sipinvestmentplanner()