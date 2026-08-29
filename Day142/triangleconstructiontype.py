import math

def triangleconstructiontype():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Invalid sides. All sides must be positive.")
        return

    sides = sorted([side1, side2, side3])

    if sides[0] + sides[1] <= sides[2]:
        print("Triangle Construction is Not Possible.")
        return

    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if math.isclose(
        sides[0] ** 2 + sides[1] ** 2,
        sides[2] ** 2,
        rel_tol=1e-9
    ):
        angle_type = "Right-Angled"
    elif sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
        angle_type = "Acute-Angled"
    else:
        angle_type = "Obtuse-Angled"

    print("\nTriangle Construction is Possible.")
    print("Type by Sides:", triangle_type)
    print("Type by Angles:", angle_type)

triangleconstructiontype()