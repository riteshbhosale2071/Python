def halfyearlycompoundinterestcalc():
    print("Half-Yearly Compound Interest Calculator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years < 0:
        print("Enter valid values.")
        return

    half_yearly_rate = rate / 2
    number_of_periods = years * 2

    amount = principal * (1 + half_yearly_rate / 100) ** number_of_periods
    compound_interest = amount - principal

    print("\nPrincipal Amount:", principal)
    print("Annual Interest Rate:", rate, "%")
    print("Half-Yearly Rate:", half_yearly_rate, "%")
    print("Time:", years, "years")
    print("Number of Compounding Periods:", number_of_periods)
    print("Compound Interest:", round(compound_interest, 2))
    print("Final Amount:", round(amount, 2))

halfyearlycompoundinterestcalc()