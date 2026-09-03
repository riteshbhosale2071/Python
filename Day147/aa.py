from fractions import Fraction

def rationalexpressionsimplification():
    print("Enter the first rational number:")
    n1 = int(input("Enter numerator: "))
    d1 = int(input("Enter denominator: "))

    print("\nEnter the second rational number:")
    n2 = int(input("Enter numerator: "))
    d2 = int(input("Enter denominator: "))

    if d1 == 0 or d2 == 0:
        print("Denominator cannot be zero.")
        return

    operation = input("Enter operation (+, -, *, /): ")

    fraction1 = Fraction(n1, d1)
    fraction2 = Fraction(n2, d2)

    if operation == "+":
        result = fraction1 + fraction2
    elif operation == "-":
        result = fraction1 - fraction2
    elif operation == "*":
        result = fraction1 * fraction2
    elif operation == "/":
        if fraction2 == 0:
            print("Cannot divide by zero.")
            return
        result = fraction1 / fraction2
    else:
        print("Invalid operation.")
        return

    print("\nRational Expression Simplification :")
    print("First Fraction:", fraction1)
    print("Second Fraction:", fraction2)
    print("Operation:", operation)
    print("Simplified Result:", result)
    print("Decimal Value:", float(result))

rationalexpressionsimplification()