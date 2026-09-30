def compoundinvestmentranking():
    print("Compound Investment Ranking :")

    number_of_investments = int(input("Enter number of investments: "))

    if number_of_investments <= 0:
        print("Number of investments must be greater than zero.")
        return

    investments = []

    for i in range(number_of_investments):
        print("\nInvestment", i + 1)

        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter number of years: "))

        if principal <= 0 or rate < 0 or years <= 0:
            print("Invalid investment details.")
            return

        amount = principal * (1 + rate / 100) ** years
        interest = amount - principal

        investments.append([i + 1, amount, interest])

    investments.sort(key=lambda x: x[1], reverse=True)

    print("\nInvestment Ranking :")

    for rank in range(len(investments)):
        investment = investments[rank]

        print("\nRank:", rank + 1)
        print("Investment:", investment[0])
        print("Compound Interest:", round(investment[2], 2))
        print("Final Amount:", round(investment[1], 2))

compoundinvestmentranking()