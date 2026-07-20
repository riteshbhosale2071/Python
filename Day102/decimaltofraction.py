def decimaltofraction():
    decimal = input("Enter a decimal number: ")
    decimal = str(decimal)

    if "." in decimal:
        whole, fraction = decimal.split(".")
        denominator = 10 ** len(fraction)
        numerator = int(whole) * denominator + int(fraction)

        print("Fraction =", numerator, "/", denominator)
    else:
        print("Enter a decimal number.")

decimaltofraction()