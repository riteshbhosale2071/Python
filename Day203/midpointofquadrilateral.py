def midpointofquadrilateral():
    print("Enter coordinates of the four vertices (x, y) in order.")

    points = []

    for i in range(1, 5):
        x = float(input(f"Enter x-coordinate of vertex {i}: "))
        y = float(input(f"Enter y-coordinate of vertex {i}: "))
        points.append((x, y))

    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    x4, y4 = points[3]

    midpoint_1 = ((x1 + x3) / 2, (y1 + y3) / 2)
    midpoint_2 = ((x2 + x4) / 2, (y2 + y4) / 2)

    print("\nMidpoint of Diagonal AC:")
    print(f"({midpoint_1[0]:.2f}, {midpoint_1[1]:.2f})")

    print("\nMidpoint of Diagonal BD:")
    print(f"({midpoint_2[0]:.2f}, {midpoint_2[1]:.2f})")

    if (
        abs(midpoint_1[0] - midpoint_2[0]) < 1e-6
        and abs(midpoint_1[1] - midpoint_2[1]) < 1e-6
    ):
        print("\nThe diagonals bisect each other.")
        print("The quadrilateral may be a parallelogram.")
    else:
        print("\nThe diagonals do not bisect each other.")

midpointofquadrilateral()