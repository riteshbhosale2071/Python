from fractions import Fraction

def rationalnumoperation():
    n1 = int(input("Enter numerator of first number: "))
    d1 = int(input("Enter denominator of first number: "))

    n2 = int(input("Enter numerator of second number: "))
    d2 = int(input("Enter denominator of second number: "))

    if d1 == 0 or d2 == 0:
        print("Denominator cannot be zero.")
        return

    r1 = Fraction(n1, d1)
    r2 = Fraction(n2, d2)

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = r1 + r2
    elif operation == "-":
        result = r1 - r2
    elif operation == "*":
        result = r1 * r2
    elif operation == "/":
        if r2 == 0:
            print("Cannot divide by zero.")
            return
        result = r1 / r2
    else:
        print("Invalid operation.")
        return

    print("Result:", result)

rationalnumoperation()