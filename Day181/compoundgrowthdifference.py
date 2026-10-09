def compoundgrowthdifference():
    print("Compound Growth Difference Analyzer :")

    initial_amount = float(input("Enter initial amount: "))
    rate1 = float(input("Enter first annual growth rate (%): "))
    rate2 = float(input("Enter second annual growth rate (%): "))
    years = int(input("Enter number of years: "))

    if initial_amount <= 0 or rate1 < 0 or rate2 < 0 or years <= 0:
        print("Enter valid values.")
        return

    amount1 = initial_amount
    amount2 = initial_amount

    print("\nYear\tGrowth 1\tGrowth 2\tDifference")

    for year in range(1, years + 1):
        amount1 = amount1 * (1 + rate1 / 100)
        amount2 = amount2 * (1 + rate2 / 100)
        difference = abs(amount1 - amount2)

        print(year, "\t", round(amount1, 2), "\t\t",
              round(amount2, 2), "\t\t", round(difference, 2))

    print("\nFinal Comparison :")
    print("Initial Amount:", round(initial_amount, 2))
    print("Final Amount at Rate 1:", round(amount1, 2))
    print("Final Amount at Rate 2:", round(amount2, 2))
    print("Final Difference:", round(abs(amount1 - amount2), 2))

    if amount1 > amount2:
        print("First growth rate produces a higher final amount.")
    elif amount2 > amount1:
        print("Second growth rate produces a higher final amount.")
    else:
        print("Both growth rates produce the same final amount.")

compoundgrowthdifference()