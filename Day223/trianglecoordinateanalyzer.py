import math

def trianglecoordinateanalyzer():
    print("Triangle Coordinate Analyzer")
    print("Enter coordinates of three vertices:")

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))
    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))
    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    ab = math.hypot(x2 - x1, y2 - y1)
    bc = math.hypot(x3 - x2, y3 - y2)
    ca = math.hypot(x1 - x3, y1 - y3)

    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    perimeter = ab + bc + ca

    print("\nSide AB =", round(ab, 2))
    print("Side BC =", round(bc, 2))
    print("Side CA =", round(ca, 2))

    if area < 1e-9:
        print("\nThe points are collinear. They do not form a triangle.")
        return

    print("\nArea =", round(area, 2))
    print("Perimeter =", round(perimeter, 2))
    print("Centroid =", (round((x1 + x2 + x3) / 3, 2), round((y1 + y2 + y3) / 3, 2)))

    sides = [ab, bc, ca]

    if math.isclose(ab, bc) and math.isclose(bc, ca):
        print("Triangle Type: Equilateral")
    elif math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab):
        print("Triangle Type: Isosceles")
    else:
        print("Triangle Type: Scalene")

    largest = max(sides)
    if math.isclose(largest ** 2, sum(s ** 2 for s in sides) - largest ** 2, rel_tol=1e-9, abs_tol=1e-9):
        print("Angle Type: Right-Angled Triangle")
    elif largest ** 2 < sum(s ** 2 for s in sides) - largest ** 2:
        print("Angle Type: Acute-Angled Triangle")
    else:
        print("Angle Type: Obtuse-Angled Triangle")

trianglecoordinateanalyzer()