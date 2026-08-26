import math

def triangleproperty():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("All sides must be positive.")
        return

    if (side1 + side2 <= side3 or
        side1 + side3 <= side2 or
        side2 + side3 <= side1):
        print("Invalid Triangle.")
        return

    sides = sorted([side1, side2, side3])
    perimeter = side1 + side2 + side3
    s = perimeter / 2

    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    if side1 == side2 == side3:
        side_type = "Equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"

    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        angle_type = "Right-Angled"
    elif sides[0]**2 + sides[1]**2 > sides[2]**2:
        angle_type = "Acute-Angled"
    else:
        angle_type = "Obtuse-Angled"

    print("\n--- Triangle Property Analysis ---")
    print("Side Type:", side_type)
    print("Angle Type:", angle_type)
    print("Perimeter:", perimeter)
    print("Area:", area)
    print("Semi-Perimeter:", s)

triangleproperty()