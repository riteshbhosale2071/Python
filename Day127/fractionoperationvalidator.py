from fractions import Fraction

def fractionoperationvalidator():
    n1 = int(input("Enter numerator of first fraction: "))
    d1 = int(input("Enter denominator of first fraction: "))

    n2 = int(input("Enter numerator of second fraction: "))
    d2 = int(input("Enter denominator of second fraction: "))

    if d1 == 0 or d2 == 0:
        print("Invalid operation: denominator cannot be zero.")
        return

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "/" and n2 == 0:
        print("Invalid operation: cannot divide by zero.")
        return

    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation.")
        return

    f1 = Fraction(n1, d1)
    f2 = Fraction(n2, d2)

    if operation == "+":
        result = f1 + f2
    elif operation == "-":
        result = f1 - f2
    elif operation == "*":
        result = f1 * f2
    else:
        result = f1 / f2

    print("Operation is Valid.")
    print("Result:", result)

fractionoperationvalidator()