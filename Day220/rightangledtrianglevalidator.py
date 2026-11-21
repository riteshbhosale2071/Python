import math

def rightangledtrianglevalidator():
    print("Right-Angled Triangle Validator")

    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if min(a, b, c) <= 0:
        print("All side lengths must be positive.")
        return

    sides = sorted([a, b, c])
    x, y, hypotenuse = sides

    if x + y <= hypotenuse:
        print("Invalid triangle: Triangle inequality is not satisfied.")
        return

    print("\nSorted Sides:")
    print("First Side =", x)
    print("Second Side =", y)
    print("Longest Side =", hypotenuse)

    left = x ** 2 + y ** 2
    right = hypotenuse ** 2

    print("\nPythagorean Theorem Verification:")
    print("a² + b² =", round(left, 4))
    print("c² =", round(right, 4))

    if math.isclose(left, right, rel_tol=1e-9):
        print("Result: The triangle is right-angled.")
    else:
        print("Result: The triangle is not right-angled.")

rightangledtrianglevalidator()