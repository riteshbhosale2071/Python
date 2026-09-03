import math
from fractions import Fraction

def rationalirrationalexpression():
    print("Rational-Irrational Expression Checker :")
    print("Supported operations: +, -, *, /")

    n1 = int(input("Enter numerator of first rational number: "))
    d1 = int(input("Enter denominator of first rational number: "))

    n2 = int(input("Enter numerator of second rational number: "))
    d2 = int(input("Enter denominator of second rational number: "))

    if d1 == 0 or d2 == 0:
        print("Denominator cannot be zero.")
        return

    operator = input("Enter operation (+, -, *, /): ")

    r1 = Fraction(n1, d1)
    r2 = Fraction(n2, d2)

    if operator == "+":
        result = r1 + r2
    elif operator == "-":
        result = r1 - r2
    elif operator == "*":
        result = r1 * r2
    elif operator == "/":
        if r2 == 0:
            print("Cannot divide by zero.")
            return
        result = r1 / r2
    else:
        print("Invalid operator.")
        return

    print("\nFirst Rational Number:", r1)
    print("Second Rational Number:", r2)
    print("Result:", result)
    print("Decimal Value:", float(result))
    print("The result is Rational.")

rationalirrationalexpression()