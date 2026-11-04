import math

def coordinatetriangleclassifier():
    x1 = float(input("Enter the X-coordinate of vertex A: "))
    y1 = float(input("Enter the Y-coordinate of vertex A: "))

    x2 = float(input("Enter the X-coordinate of vertex B: "))
    y2 = float(input("Enter the Y-coordinate of vertex B: "))

    x3 = float(input("Enter the X-coordinate of vertex C: "))
    y3 = float(input("Enter the Y-coordinate of vertex C: "))

    side1 = math.hypot(x2 - x1, y2 - y1)
    side2 = math.hypot(x3 - x2, y3 - y2)
    side3 = math.hypot(x1 - x3, y1 - y3)

    sides = sorted([side1, side2, side3])

    if math.isclose(sides[0] + sides[1], sides[2], rel_tol=1e-9, abs_tol=1e-9):
        print("The points do not form a valid triangle.")
        return

    if math.isclose(side1, side2, rel_tol=1e-9, abs_tol=1e-9) and math.isclose(
        side2, side3, rel_tol=1e-9, abs_tol=1e-9
    ):
        triangle_type = "Equilateral"
    elif (
        math.isclose(side1, side2, rel_tol=1e-9, abs_tol=1e-9)
        or math.isclose(side2, side3, rel_tol=1e-9, abs_tol=1e-9)
        or math.isclose(side1, side3, rel_tol=1e-9, abs_tol=1e-9)
    ):
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    if math.isclose(
        sides[0] ** 2 + sides[1] ** 2,
        sides[2] ** 2,
        rel_tol=1e-9,
        abs_tol=1e-9
    ):
        angle_type = "Right-angled"
    elif sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
        angle_type = "Acute-angled"
    else:
        angle_type = "Obtuse-angled"

    print(f"Side AB: {side1:.2f}")
    print(f"Side BC: {side2:.2f}")
    print(f"Side CA: {side3:.2f}")
    print(f"Triangle Type: {triangle_type}")
    print(f"Angle Classification: {angle_type}")

coordinatetriangleclassifier()