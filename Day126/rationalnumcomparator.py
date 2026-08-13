from fractions import Fraction

def rationalnumbercomparator():
    n1 = int(input("Enter numerator of first number: "))
    d1 = int(input("Enter denominator of first number: "))

    n2 = int(input("Enter numerator of second number: "))
    d2 = int(input("Enter denominator of second number: "))

    if d1 == 0 or d2 == 0:
        print("Denominator cannot be zero.")
        return

    r1 = Fraction(n1, d1)
    r2 = Fraction(n2, d2)

    print("First Rational Number:", r1)
    print("Second Rational Number:", r2)

    if r1 > r2:
        print("First rational number is greater.")
    elif r1 < r2:
        print("Second rational number is greater.")
    else:
        print("Both rational numbers are equal.")

rationalnumbercomparator()