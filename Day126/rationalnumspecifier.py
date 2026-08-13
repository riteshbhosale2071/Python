from fractions import Fraction

def rationalnumsimplifier():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    simplified = Fraction(numerator, denominator)

    print("Simplified Rational Number:", simplified)

rationalnumsimplifier()