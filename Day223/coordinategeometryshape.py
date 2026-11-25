import math

def coordinategeometryshape():
    print("Coordinate Geometry Shape Identifier")
    print("Enter coordinates of four vertices in order.")

    points = []

    for i in range(1, 5):
        x = float(input(f"Enter x-coordinate of point {i}: "))
        y = float(input(f"Enter y-coordinate of point {i}: "))
        points.append((x, y))

    def distance(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    sides = [
        distance(points[0], points[1]),
        distance(points[1], points[2]),
        distance(points[2], points[3]),
        distance(points[3], points[0])
    ]

    diagonals = [
        distance(points[0], points[2]),
        distance(points[1], points[3])
    ]

    area = abs(sum(
        points[i][0] * points[(i + 1) % 4][1] -
        points[(i + 1) % 4][0] * points[i][1]
        for i in range(4)
    )) / 2

    if area < 1e-9:
        print("The points do not form a valid quadrilateral.")
        return

    def equal(a, b):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)

    def dot(p1, p2, p3):
        return ((p1[0] - p2[0]) * (p3[0] - p2[0]) +
                (p1[1] - p2[1]) * (p3[1] - p2[1]))

    right_angles = all(
        equal(dot(points[i - 1], points[i], points[(i + 1) % 4]), 0)
        for i in range(4)
    )

    opposite_sides_equal = equal(sides[0], sides[2]) and equal(sides[1], sides[3])
    all_sides_equal = all(equal(sides[0], side) for side in sides[1:])
    opposite_sides_parallel = (
        equal((points[1][0] - points[0][0]) * (points[3][1] - points[2][1]),
              (points[1][1] - points[0][1]) * (points[3][0] - points[2][0])) and
        equal((points[2][0] - points[1][0]) * (points[0][1] - points[3][1]),
              (points[2][1] - points[1][1]) * (points[0][0] - points[3][0]))
    )

    print("\nSide Lengths:", [round(side, 2) for side in sides])
    print("Diagonal Lengths:", [round(d, 2) for d in diagonals])
    print("Area =", round(area, 2))

    if all_sides_equal and right_angles:
        print("Shape: Square")
    elif right_angles and opposite_sides_equal:
        print("Shape: Rectangle")
    elif all_sides_equal:
        print("Shape: Rhombus")
    elif opposite_sides_equal and opposite_sides_parallel:
        print("Shape: Parallelogram")
    elif equal(sides[0], sides[1]) and equal(sides[2], sides[3]):
        print("Shape: Kite or possible other quadrilateral")
    elif opposite_sides_parallel:
        print("Shape: Trapezoid")
    else:
        print("Shape: Irregular Quadrilateral")

coordinategeometryshape()