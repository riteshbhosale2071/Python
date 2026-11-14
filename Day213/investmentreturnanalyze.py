def investmentreturnanalyze():
    try:
        investment_name = input("Enter investment name: ")
        initial_investment = float(input("Enter initial investment amount (₹): "))
        final_value = float(input("Enter current or final investment value (₹): "))
        investment_years = float(input("Enter investment duration (years): "))

        if initial_investment <= 0 or final_value < 0 or investment_years <= 0:
            print("Please enter valid investment details.")
            return

        profit_loss = final_value - initial_investment
        return_percentage = (profit_loss / initial_investment) * 100

        annualized_return = (
            (final_value / initial_investment) ** (1 / investment_years) - 1
        ) * 100 if final_value > 0 else -100

        print("\nInvestment Return Analysis")
        print("Investment Name:", investment_name)
        print("Initial Investment: ₹", round(initial_investment, 2))
        print("Final Investment Value: ₹", round(final_value, 2))
        print("Investment Duration:", investment_years, "years")

        if profit_loss > 0:
            print("Total Profit: ₹", round(profit_loss, 2))
        elif profit_loss < 0:
            print("Total Loss: ₹", round(abs(profit_loss), 2))
        else:
            print("Result: No Profit, No Loss")

        print("Total Return:", round(return_percentage, 2), "%")
        print("Annualized Return (CAGR):", round(annualized_return, 2), "%")

        if return_percentage > 0:
            print("Investment Performance: Positive Return")
        elif return_percentage < 0:
            print("Investment Performance: Negative Return")
        else:
            print("Investment Performance: Break-even")

    except ValueError:
        print("Please enter valid numeric values.")

investmentreturnanalyze()