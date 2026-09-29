def quarterlycompoundinterest():
    print("Quarterly Compound Interest Calculator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years < 0:
        print("Enter valid values.")
        return

    quarterly_rate = rate / 4
    number_of_periods = years * 4

    amount = principal * (1 + quarterly_rate / 100) ** number_of_periods
    compound_interest = amount - principal

    print("\nPrincipal Amount:", principal)
    print("Annual Interest Rate:", rate, "%")
    print("Quarterly Rate:", quarterly_rate, "%")
    print("Time:", years, "years")
    print("Number of Compounding Periods:", number_of_periods)
    print("Compound Interest:", round(compound_interest, 2))
    print("Final Amount:", round(amount, 2))

quarterlycompoundinterest()