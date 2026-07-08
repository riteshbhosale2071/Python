def fractionanalyzer():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    print("Fraction:", numerator, "/", denominator)

    if numerator < denominator:
        print("Type: Proper Fraction")
    elif numerator == denominator:
        print("Type: Equal to 1")
    else:
        print("Type: Improper Fraction")

fractionanalyzer()