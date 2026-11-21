import math

def converseofpythagorastheorem():
    print("Converse of Pythagoras Theorem Checker")

    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if min(a, b, c) <= 0:
        print("All side lengths must be positive.")
        return

    sides = sorted([a, b, c])
    x, y, z = sides

    if x + y <= z:
        print("Invalid triangle: Triangle inequality is not satisfied.")
        return

    print("\nArranged Sides:")
    print("First Side =", x)
    print("Second Side =", y)
    print("Longest Side =", z)

    left = x ** 2 + y ** 2
    right = z ** 2

    print("\nConverse of Pythagoras Theorem:")
    print("a² + b² =", round(left, 4))
    print("c² =", round(right, 4))

    if math.isclose(left, right, rel_tol=1e-9):
        print("\nResult: The triangle is right-angled.")
        print("The Converse of Pythagoras Theorem is verified.")
    else:
        print("\nResult: The triangle is not right-angled.")
        print("The Converse of Pythagoras Theorem is not verified.")

converseofpythagorastheorem()