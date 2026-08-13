from fractions import Fraction

def rationalnumberequivalent():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    count = int(input("Enter number of equivalent forms: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    if count <= 0:
        print("Enter a positive number of forms.")
        return

    number = Fraction(numerator, denominator)

    print("Equivalent Rational Numbers:")

    for i in range(1, count + 1):
        new_numerator = number.numerator * i
        new_denominator = number.denominator * i
        print(f"{new_numerator}/{new_denominator}")

rationalnumberequivalent()