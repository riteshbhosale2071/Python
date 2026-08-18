def investmentprofitdistributor():
    total_profit = float(input("Enter total profit: "))

    investments = list(map(float, input("Enter investments of all partners separated by spaces: ").split()))

    if total_profit < 0 or not investments or any(i <= 0 for i in investments):
        print("Please enter valid positive investments.")
        return

    total_investment = sum(investments)

    print("\nProfit Distribution:")

    for i, investment in enumerate(investments, start=1):
        share = (investment / total_investment) * total_profit
        print(f"Partner {i}: {share:.2f}")

investmentprofitdistributor()