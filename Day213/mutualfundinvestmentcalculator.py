def mutualfundinvestmentcalculator():
    try:
        investor_name = input("Enter investor name: ")
        investment_type = input("Enter investment type (SIP or Lumpsum): ").strip().upper()

        if investment_type == "SIP":
            monthly_investment = float(input("Enter monthly investment (₹): "))
            annual_return = float(input("Enter expected annual return (%): "))
            years = int(input("Enter investment period (years): "))

            if monthly_investment <= 0 or annual_return < 0 or years <= 0:
                print("Please enter valid investment details.")
                return

            monthly_rate = annual_return / (12 * 100)
            months = years * 12
            invested_amount = monthly_investment * months

            if monthly_rate == 0:
                future_value = invested_amount
            else:
                future_value = monthly_investment * (
                    ((1 + monthly_rate) ** months - 1) / monthly_rate
                ) * (1 + monthly_rate)

        elif investment_type == "LUMPSUM":
            investment = float(input("Enter one-time investment (₹): "))
            annual_return = float(input("Enter expected annual return (%): "))
            years = int(input("Enter investment period (years): "))

            if investment <= 0 or annual_return < 0 or years <= 0:
                print("Please enter valid investment details.")
                return

            invested_amount = investment
            future_value = investment * (1 + annual_return / 100) ** years

        else:
            print("Invalid investment type. Choose SIP or Lumpsum.")
            return

        estimated_profit = future_value - invested_amount
        return_percentage = (estimated_profit / invested_amount) * 100

        print("\nMutual Fund Investment Report")
        print("Investor Name:", investor_name)
        print("Investment Type:", investment_type)
        print("Total Invested Amount: ₹", round(invested_amount, 2))
        print("Estimated Future Value: ₹", round(future_value, 2))
        print("Estimated Profit: ₹", round(estimated_profit, 2))
        print("Estimated Return:", round(return_percentage, 2), "%")
        print("\nNote: Returns are estimates, not guaranteed.")

    except ValueError:
        print("Please enter valid numeric values.")

mutualfundinvestmentcalculator()