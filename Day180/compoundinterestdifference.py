def compoundinterestdifference():
    print("Compound Interest Difference :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    simple_interest = principal * rate * years / 100
    simple_amount = principal + simple_interest

    compound_amount = principal

    print("\nYear\tSimple Amount\tCompound Amount\tDifference")

    for year in range(1, years + 1):
        simple_amount_year = principal + (principal * rate * year / 100)
        compound_amount = principal * (1 + rate / 100) ** year
        difference = compound_amount - simple_amount_year

        print(year, "\t", round(simple_amount_year, 2), "\t\t", round(compound_amount, 2), "\t\t", round(difference, 2))

    final_difference = compound_amount - simple_amount

    print("\nSummary :")
    print("Simple Interest Amount:", round(simple_amount, 2))
    print("Compound Interest Amount:", round(compound_amount, 2))
    print("Final Difference:", round(final_difference, 2))

compoundinterestdifference()