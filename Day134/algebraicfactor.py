import math

def algebraicfactor():
    a = int(input("Enter coefficient of x²: "))
    b = int(input("Enter coefficient of x: "))
    c = int(input("Enter constant: "))

    discriminant = b ** 2 - 4 * a * c

    if a == 0:
        print("This is not a quadratic expression.")
        return

    if discriminant < 0:
        print("No real factors found.")
        return

    sqrt_d = math.isqrt(discriminant)

    if sqrt_d ** 2 != discriminant:
        print("Expression cannot be factored into integer factors.")
        return

    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)

    print("Factor 1: (x -", root1, ")")
    print("Factor 2: (x -", root2, ")")

algebraicfactor()