def compoundinterestformula():
    print("Compound Interest Formula Generator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))
    frequency = int(input("Enter number of times compounded per year: "))

    if principal <= 0 or rate < 0 or years <= 0 or frequency <= 0:
        print("Enter valid values.")
        return

    periodic_rate = rate / (100 * frequency)
    total_periods = frequency * years

    amount = principal * (1 + periodic_rate) ** total_periods
    compound_interest = amount - principal

    print("\nFormula Details :")
    print("Formula: A = P(1 + r/n)^(nt)")
    print("P =", principal)
    print("r =", rate, "%")
    print("n =", frequency)
    print("t =", years)

    print("\nPeriodic Interest Rate:", round(periodic_rate * 100, 4), "%")
    print("Total Compounding Periods:", total_periods)
    print("Final Amount:", round(amount, 2))
    print("Compound Interest:", round(compound_interest, 2))

compoundinterestformula()