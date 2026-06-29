def equivalentfraction():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    multiplier = int(input("Enter multiplier: "))

    new_numerator = numerator * multiplier
    new_denominator = denominator * multiplier

    print("Original Fraction =", numerator, "/", denominator)
    print("Equivalent Fraction =", new_numerator, "/", new_denominator)

equivalentfraction()