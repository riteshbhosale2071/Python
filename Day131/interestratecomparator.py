def interestratecomparator():
    principal1 = float(input("Enter principal amount 1: "))
    interest1 = float(input("Enter interest amount 1: "))

    principal2 = float(input("Enter principal amount 2: "))
    interest2 = float(input("Enter interest amount 2: "))

    if principal1 <= 0 or principal2 <= 0 or interest1 < 0 or interest2 < 0:
        print("Please enter valid values.")
        return

    rate1 = (interest1 / principal1) * 100
    rate2 = (interest2 / principal2) * 100

    print("Interest Rate 1:", rate1, "%")
    print("Interest Rate 2:", rate2, "%")

    if rate1 > rate2:
        print("Interest Rate 1 is higher.")
    elif rate1 < rate2:
        print("Interest Rate 2 is higher.")
    else:
        print("Both interest rates are equal.")

interestratecomparator()