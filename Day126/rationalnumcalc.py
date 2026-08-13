from fractions import Fraction

def rationalnumcalc():
    n1 = int(input("Enter numerator of first number: "))
    d1 = int(input("Enter denominator of first number: "))

    n2 = int(input("Enter numerator of second number: "))
    d2 = int(input("Enter denominator of second number: "))

    if d1 == 0 or d2 == 0:
        print("Denominator cannot be zero.")
        return

    r1 = Fraction(n1, d1)
    r2 = Fraction(n2, d2)

    print("Addition:", r1 + r2)
    print("Subtraction:", r1 - r2)
    print("Multiplication:", r1 * r2)

    if r2 != 0:
        print("Division:", r1 / r2)
    else:
        print("Division: Cannot divide by zero.")

rationalnumcalc()