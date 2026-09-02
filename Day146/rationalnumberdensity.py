from fractions import Fraction

def rationalnumberdensity():
    numerator1 = int(input("Enter numerator of first rational number: "))
    denominator1 = int(input("Enter denominator of first rational number: "))

    numerator2 = int(input("Enter numerator of second rational number: "))
    denominator2 = int(input("Enter denominator of second rational number: "))

    if denominator1 == 0 or denominator2 == 0:
        print("Denominator cannot be zero.")
        return

    r1 = Fraction(numerator1, denominator1)
    r2 = Fraction(numerator2, denominator2)

    if r1 >= r2:
        print("The first rational number must be smaller than the second.")
        return

    middle = (r1 + r2) / 2

    print("\nFirst Rational Number:", r1)
    print("Second Rational Number:", r2)
    print("A Rational Number Between Them:", middle)

rationalnumberdensity()