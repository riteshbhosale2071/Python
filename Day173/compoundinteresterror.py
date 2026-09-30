def compoundinteresterror():
    print("Compound Interest Error Checker :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))
    calculated_amount = float(input("Enter calculated final amount: "))

    if principal <= 0:
        print("Error: Principal amount must be greater than zero.")
        return

    if rate < 0:
        print("Error: Interest rate cannot be negative.")
        return

    if years <= 0:
        print("Error: Number of years must be greater than zero.")
        return

    if calculated_amount <= 0:
        print("Error: Calculated amount must be greater than zero.")
        return

    correct_amount = principal * (1 + rate / 100) ** years
    difference = abs(correct_amount - calculated_amount)

    print("\nExpected Final Amount:", round(correct_amount, 2))
    print("Entered Final Amount:", round(calculated_amount, 2))
    print("Difference:", round(difference, 2))

    if difference < 0.01:
        print("No significant error found.")
    elif calculated_amount < correct_amount:
        print("Error: The entered final amount is lower than the correct amount.")
    else:
        print("Error: The entered final amount is higher than the correct amount.")

compoundinteresterror()