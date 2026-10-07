def annualgrowthtable():
    print("Annual Growth Table :")

    principal = float(input("Enter initial amount: "))
    rate = float(input("Enter annual growth rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    amount = principal

    print("\nYear\tAmount\t\tGrowth")

    for year in range(1, years + 1):
        previous_amount = amount
        amount = amount * (1 + rate / 100)
        growth = amount - previous_amount

        print(year, "\t", round(amount, 2), "\t\t", round(growth, 2))

    total_growth = amount - principal
    growth_percentage = (total_growth / principal) * 100

    print("\nSummary :")
    print("Initial Amount:", round(principal, 2))
    print("Final Amount:", round(amount, 2))
    print("Total Growth:", round(total_growth, 2))
    print("Growth Percentage:", round(growth_percentage, 2), "%")

annualgrowthtable()