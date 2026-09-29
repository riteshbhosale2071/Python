def compoundingfrequencycomparator():
    print("Compounding Frequency Comparator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years < 0:
        print("Enter valid values.")
        return

    annual_amount = principal * (1 + rate / 100) ** years

    half_yearly_amount = principal * (1 + rate / 200) ** (years * 2)

    quarterly_amount = principal * (1 + rate / 400) ** (years * 4)

    monthly_amount = principal * (1 + rate / 1200) ** (years * 12)

    annual_interest = annual_amount - principal
    half_yearly_interest = half_yearly_amount - principal
    quarterly_interest = quarterly_amount - principal
    monthly_interest = monthly_amount - principal

    print("\nResults :")

    print("\nAnnual Compounding:")
    print("Compound Interest:", round(annual_interest, 2))
    print("Final Amount:", round(annual_amount, 2))

    print("\nHalf-Yearly Compounding:")
    print("Compound Interest:", round(half_yearly_interest, 2))
    print("Final Amount:", round(half_yearly_amount, 2))

    print("\nQuarterly Compounding:")
    print("Compound Interest:", round(quarterly_interest, 2))
    print("Final Amount:", round(quarterly_amount, 2))

    print("\nMonthly Compounding:")
    print("Compound Interest:", round(monthly_interest, 2))
    print("Final Amount:", round(monthly_amount, 2))

    print("\nComparison :")
    amounts = [annual_amount, half_yearly_amount, quarterly_amount, monthly_amount]
    highest_amount = max(amounts)

    if highest_amount == annual_amount:
        print("Highest final amount: Annual Compounding")
    elif highest_amount == half_yearly_amount:
        print("Highest final amount: Half-Yearly Compounding")
    elif highest_amount == quarterly_amount:
        print("Highest final amount: Quarterly Compounding")
    else:
        print("Highest final amount: Monthly Compounding")

compoundingfrequencycomparator()