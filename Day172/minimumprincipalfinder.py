def minimumprincipalfinder():
    print("Minimum Principal Finder :")

    target = float(input("Enter target amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if target <= 0 or rate <= 0 or years <= 0:
        print("Enter valid values.")
        return

    minimum_principal = target / ((1 + rate / 100) ** years)

    print("\nTarget Amount:", round(target, 2))
    print("Annual Interest Rate:", rate, "%")
    print("Time:", years, "years")
    print("Minimum Principal Required:", round(minimum_principal, 2))

minimumprincipalfinder()