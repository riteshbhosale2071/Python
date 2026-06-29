def mixedfraction():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    whole = numerator // denominator
    remainder = numerator % denominator

    if remainder == 0:
        print("Mixed Fraction =", whole)
    else:
        print("Mixed Fraction =", whole, remainder, "/", denominator)

mixedfraction()