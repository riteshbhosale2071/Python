def compoundvssimpleinterest():
    print("Compound-vs-Simple Interest Analyzer :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years < 0:
        print("Enter valid values.")
        return

    simple_interest = principal * rate * years / 100
    simple_amount = principal + simple_interest

    compound_amount = principal * (1 + rate / 100) ** years
    compound_interest = compound_amount - principal

    difference = compound_interest - simple_interest

    print("\nSimple Interest :")
    print("Simple Interest:", round(simple_interest, 2))
    print("Final Amount:", round(simple_amount, 2))

    print("\nCompound Interest :")
    print("Compound Interest:", round(compound_interest, 2))
    print("Final Amount:", round(compound_amount, 2))

    print("\nComparison :")
    print("Difference in Interest:", round(difference, 2))

    if compound_interest > simple_interest:
        print("Compound Interest is greater than Simple Interest.")
    elif compound_interest < simple_interest:
        print("Simple Interest is greater than Compound Interest.")
    else:
        print("Both interests are equal.")

compoundvssimpleinterest()