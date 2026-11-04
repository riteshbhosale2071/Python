import math

def coordinatequadrilateralclassifier():
    points = []

    for i in range(4):
        x = float(input(f"Enter X-coordinate of vertex {i + 1}: "))
        y = float(input(f"Enter Y-coordinate of vertex {i + 1}: "))
        points.append((x, y))

    def distance(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    sides = [
        distance(points[0], points[1]),
        distance(points[1], points[2]),
        distance(points[2], points[3]),
        distance(points[3], points[0])
    ]

    diagonal1 = distance(points[0], points[2])
    diagonal2 = distance(points[1], points[3])

    def parallel(p1, p2, p3, p4):
        dx1 = p2[0] - p1[0]
        dy1 = p2[1] - p1[1]
        dx2 = p4[0] - p3[0]
        dy2 = p4[1] - p3[1]

        return math.isclose(
            dx1 * dy2 - dy1 * dx2, 0,
            rel_tol=1e-9, abs_tol=1e-9
        )

    def equal(a, b):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)

    opposite1_parallel = parallel(points[0], points[1], points[2], points[3])
    opposite2_parallel = parallel(points[1], points[2], points[3], points[0])

    all_sides_equal = all(equal(sides[0], side) for side in sides[1:])
    opposite_sides_equal = equal(sides[0], sides[2]) and equal(sides[1], sides[3])
    diagonals_equal = equal(diagonal1, diagonal2)

    if not (opposite1_parallel or opposite2_parallel):
        classification = "General Quadrilateral"
    elif opposite1_parallel and opposite2_parallel:
        if all_sides_equal and diagonals_equal:
            classification = "Square"
        elif all_sides_equal:
            classification = "Rhombus"
        elif diagonals_equal and equal(sides[0], sides[2]) and equal(sides[1], sides[3]):
            classification = "Rectangle"
        else:
            classification = "Parallelogram"
    else:
        classification = "Trapezoid"

    print("\nQuadrilateral Classification :")
    for i, side in enumerate(sides, start=1):
        print(f"Side {i}: {side:.2f} units")

    print(f"Diagonal 1: {diagonal1:.2f} units")
    print(f"Diagonal 2: {diagonal2:.2f} units")
    print(f"Classification: {classification}")

coordinatequadrilateralclassifier()