def compoundratecomparison():
    print("Compound Rate Comparison :")

    principal = float(input("Enter principal amount: "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or years <= 0:
        print("Enter valid values.")
        return

    rate1 = float(input("Enter first annual interest rate (%): "))
    rate2 = float(input("Enter second annual interest rate (%): "))

    if rate1 < 0 or rate2 < 0:
        print("Interest rates cannot be negative.")
        return

    amount1 = principal * (1 + rate1 / 100) ** years
    amount2 = principal * (1 + rate2 / 100) ** years

    interest1 = amount1 - principal
    interest2 = amount2 - principal

    print("\nComparison :")
    print("Rate 1:", rate1, "%")
    print("Final Amount:", round(amount1, 2))
    print("Compound Interest:", round(interest1, 2))

    print("\nRate 2:", rate2, "%")
    print("Final Amount:", round(amount2, 2))
    print("Compound Interest:", round(interest2, 2))

    if amount1 > amount2:
        print("\nRate 1 produces a higher final amount.")
        print("Difference:", round(amount1 - amount2, 2))
    elif amount2 > amount1:
        print("\nRate 2 produces a higher final amount.")
        print("Difference:", round(amount2 - amount1, 2))
    else:
        print("\nBoth rates produce the same final amount.")

compoundratecomparison()