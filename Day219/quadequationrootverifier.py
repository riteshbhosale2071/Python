import math

def quadequationrootverifier():
    print("Quadratic Equation Root Verifier")
    print("Standard Form: ax² + bx + c = 0")

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    if a == 0:
        print("Invalid quadratic equation: a cannot be zero.")
        return

    print("\nEnter the two roots to verify:")
    root1 = float(input("Enter first root: "))
    root2 = float(input("Enter second root: "))

    value1 = a * root1 ** 2 + b * root1 + c
    value2 = a * root2 ** 2 + b * root2 + c

    print("\nVerification Results:")
    print("Polynomial value at root 1 =", round(value1, 6))
    print("Polynomial value at root 2 =", round(value2, 6))

    if math.isclose(value1, 0, abs_tol=1e-9) and math.isclose(value2, 0, abs_tol=1e-9):
        print("Both values are verified as roots of the equation.")
    else:
        print("The entered values are not both roots of the equation.")

    print("\nSum of entered roots =", round(root1 + root2, 4))
    print("Product of entered roots =", round(root1 * root2, 4))
    print("Expected sum of roots =", round(-b / a, 4))
    print("Expected product of roots =", round(c / a, 4))

quadequationrootverifier()