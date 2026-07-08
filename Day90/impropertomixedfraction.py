def impropertomixed():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    whole = numerator // denominator
    remainder = numerator % denominator

    print("Mixed Fraction:", whole, remainder, "/", denominator)

impropertomixed()