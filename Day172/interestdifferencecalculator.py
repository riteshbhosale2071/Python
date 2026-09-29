def interestdifferencecalculator():
    print("Interest Difference Calculator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years < 0:
        print("Enter valid values.")
        return

    simple_interest = principal * rate * years / 100

    compound_amount = principal * (1 + rate / 100) ** years
    compound_interest = compound_amount - principal

    difference = abs(compound_interest - simple_interest)

    print("\nSimple Interest:", round(simple_interest, 2))
    print("Compound Interest:", round(compound_interest, 2))
    print("Interest Difference:", round(difference, 2))

    if compound_interest > simple_interest:
        print("Compound Interest is greater by:", round(difference, 2))
    elif simple_interest > compound_interest:
        print("Simple Interest is greater by:", round(difference, 2))
    else:
        print("Both interests are equal.")

interestdifferencecalculator()