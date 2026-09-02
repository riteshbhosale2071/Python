def rationalnumdecimal():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    decimal = numerator / denominator

    print("Rational Number:", numerator, "/", denominator)
    print("Decimal Value:", decimal)

rationalnumdecimal()