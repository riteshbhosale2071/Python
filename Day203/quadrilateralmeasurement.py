import math

def quadrilateralmeasurement():
    print("Enter the coordinates of the four vertices in order.")

    points = []

    for i in range(1, 5):
        x = float(input(f"Enter x-coordinate of vertex {i}: "))
        y = float(input(f"Enter y-coordinate of vertex {i}: "))
        points.append((x, y))

    sides = []

    for i in range(4):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 4]

        side = math.dist((x1, y1), (x2, y2))
        sides.append(side)

    perimeter = sum(sides)

    area = abs(
        sum(
            points[i][0] * points[(i + 1) % 4][1]
            - points[(i + 1) % 4][0] * points[i][1]
            for i in range(4)
        )
    ) / 2

    diagonal_ac = math.dist(points[0], points[2])
    diagonal_bd = math.dist(points[1], points[3])

    if area == 0:
        print("Invalid quadrilateral. The vertices may be collinear.")
        return

    print("\nQuadrilateral Measurement Report")
    for i, side in enumerate(sides, start=1):
        print(f"Side {i}: {side:.2f}")

    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Diagonal AC: {diagonal_ac:.2f}")
    print(f"Diagonal BD: {diagonal_bd:.2f}")

    if all(math.isclose(side, sides[0], rel_tol=1e-6) for side in sides):
        print("Side Classification: All sides are equal.")
    elif (
        math.isclose(sides[0], sides[2], rel_tol=1e-6)
        and math.isclose(sides[1], sides[3], rel_tol=1e-6)
    ):
        print("Side Classification: Opposite sides are equal.")
    else:
        print("Side Classification: General quadrilateral.")

quadrilateralmeasurement()