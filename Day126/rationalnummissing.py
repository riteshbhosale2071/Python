from fractions import Fraction

def rationalnumbermissing():
    print("Equation: a/b + x = c/d")

    a = int(input("Enter numerator of first fraction: "))
    b = int(input("Enter denominator of first fraction: "))
    c = int(input("Enter numerator of result fraction: "))
    d = int(input("Enter denominator of result fraction: "))

    if b == 0 or d == 0:
        print("Denominator cannot be zero.")
        return

    first = Fraction(a, b)
    result = Fraction(c, d)
    missing = result - first

    print("Missing Rational Number:", missing)

rationalnumbermissing()