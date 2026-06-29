def convert():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
    else:
        decimal = numerator / denominator
        print("Decimal Value =", round(decimal, 4))

convert()