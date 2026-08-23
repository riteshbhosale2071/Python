import math

def squarerootverification():
    number = float(input("Enter a number: "))
    root = float(input("Enter the claimed square root: "))

    if number < 0:
        print("Square root is not defined for negative numbers.")
        return

    if math.isclose(root * root, number, rel_tol=1e-9):
        print("The given value is a correct square root.")
    else:
        print("The given value is not a correct square root.")

squarerootverification()