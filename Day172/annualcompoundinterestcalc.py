def annualcompoundinterestcalc():
    print("Annual Compound Interest Calculator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years < 0:
        print("Enter valid values.")
        return

    amount = principal * (1 + rate / 100) ** years
    compound_interest = amount - principal

    print("\nPrincipal Amount:", principal)
    print("Annual Interest Rate:", rate, "%")
    print("Time:", years, "years")
    print("Compound Interest:", round(compound_interest, 2))
    print("Final Amount:", round(amount, 2))

annualcompoundinterestcalc()