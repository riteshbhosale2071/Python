import math

def pythagoreantripletchecker():
    print("Pythagorean Triplet Checker")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    if min(a, b, c) <= 0:
        print("All numbers must be positive integers.")
        return

    sides = sorted([a, b, c])
    x, y, z = sides

    print("\nArranged Triplet:", x, y, z)

    if x ** 2 + y ** 2 == z ** 2:
        print("Result: The numbers form a Pythagorean triplet.")
        print(f"{x}² + {y}² = {z}²")
    else:
        print("Result: The numbers do not form a Pythagorean triplet.")
        print("a² + b² =", x ** 2 + y ** 2)
        print("c² =", z ** 2)

pythagoreantripletchecker()