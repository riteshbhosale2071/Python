def investmentportfoliоanalyzer():
    print("Investment Portfolio Analyzer")

    n = int(input("Enter the number of investments: "))

    if n <= 0:
        print("Please enter a positive number of investments.")
        return

    investments = []
    total_investment = 0
    total_current_value = 0

    for i in range(n):
        print(f"\nInvestment {i + 1}")
        name = input("Enter investment name: ")
        invested_amount = float(input("Enter invested amount: "))
        current_value = float(input("Enter current value: "))

        if invested_amount <= 0 or current_value < 0:
            print("Invalid investment details.")
            return

        profit_loss = current_value - invested_amount
        return_percentage = (profit_loss / invested_amount) * 100

        investments.append((name, invested_amount, current_value, profit_loss, return_percentage))

        total_investment += invested_amount
        total_current_value += current_value

    total_profit_loss = total_current_value - total_investment
    overall_return = (total_profit_loss / total_investment) * 100

    print("\nInvestment Portfolio Summary:")
    print(f"{'Investment':<20}{'Invested':<15}{'Current Value':<15}{'Profit/Loss':<15}{'Return %':<12}")

    for investment in investments:
        name, invested, current, profit_loss, percentage = investment
        print(f"{name:<20}{invested:<15.2f}{current:<15.2f}{profit_loss:<15.2f}{percentage:<12.2f}")

    print("\nPortfolio Analysis:")
    print("Total Invested:", round(total_investment, 2))
    print("Total Current Value:", round(total_current_value, 2))
    print("Total Profit/Loss:", round(total_profit_loss, 2))
    print("Overall Return:", round(overall_return, 2), "%")

    if total_profit_loss > 0:
        print("Portfolio Status: Profit")
    elif total_profit_loss < 0:
        print("Portfolio Status: Loss")
    else:
        print("Portfolio Status: No Profit, No Loss")

investmentportfoliоanalyzer()