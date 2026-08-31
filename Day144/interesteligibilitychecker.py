def interesteligibilitychecker():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate (%): "))
    time = float(input("Enter time (years): "))
    minimum_interest = float(input("Enter minimum required interest: "))

    if principal <= 0 or rate < 0 or time < 0 or minimum_interest < 0:
        print("Enter valid values.")
        return

    interest = (principal * rate * time) / 100

    print("Calculated Interest:", interest)

    if interest >= minimum_interest:
        print("Eligible: Interest meets the required amount.")
    else:
        print("Not Eligible: Interest is below the required amount.")

interesteligibilitychecker()