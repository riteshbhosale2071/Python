import math

def righttrianglevalidator():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("All sides must be positive.")
        return

    sides = sorted([side1, side2, side3])

    if sides[0] + sides[1] <= sides[2]:
        print("These sides cannot form a triangle.")
        return

    if math.isclose(
        sides[0] ** 2 + sides[1] ** 2,
        sides[2] ** 2
    ):
        print("The triangle is a Right Triangle.")
    else:
        print("The triangle is not a Right Triangle.")

righttrianglevalidator()