def investmentcomparison():
    print("Investment Comparison :")

    number_of_investments = int(input("Enter number of investments: "))

    if number_of_investments <= 0:
        print("Enter a valid number of investments.")
        return

    investments = []

    for i in range(number_of_investments):
        print("\nInvestment", i + 1)

        name = input("Enter investment name: ")
        principal = float(input("Enter initial investment: "))
        rate = float(input("Enter annual return rate (%): "))
        years = float(input("Enter investment period in years: "))

        if principal <= 0 or rate < 0 or years <= 0:
            print("Enter valid investment details.")
            return

        final_amount = principal * (1 + rate / 100) ** years
        profit = final_amount - principal

        investments.append([name, principal, rate, years, final_amount, profit])

    print("\nInvestment Comparison :")

    for investment in investments:
        print("\nInvestment:", investment[0])
        print("Initial Investment:", round(investment[1], 2))
        print("Annual Return:", round(investment[2], 2), "%")
        print("Period:", round(investment[3], 2), "years")
        print("Final Amount:", round(investment[4], 2))
        print("Profit:", round(investment[5], 2))

    best_investment = max(investments, key=lambda x: x[5])

    print("\nBest Investment :")
    print("Investment:", best_investment[0])
    print("Highest Profit:", round(best_investment[5], 2))
    print("Final Amount:", round(best_investment[4], 2))

investmentcomparison()