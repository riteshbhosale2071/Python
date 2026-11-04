def triangleareafromcoordinates():
    x1 = float(input("Enter the X-coordinate of vertex A: "))
    y1 = float(input("Enter the Y-coordinate of vertex A: "))

    x2 = float(input("Enter the X-coordinate of vertex B: "))
    y2 = float(input("Enter the Y-coordinate of vertex B: "))

    x3 = float(input("Enter the X-coordinate of vertex C: "))
    y3 = float(input("Enter the Y-coordinate of vertex C: "))

    area = abs(
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    ) / 2

    print(f"Vertex A: ({x1:.2f}, {y1:.2f})")
    print(f"Vertex B: ({x2:.2f}, {y2:.2f})")
    print(f"Vertex C: ({x3:.2f}, {y3:.2f})")

    if area == 0:
        print("The points are collinear. Triangle area is zero.")
    else:
        print(f"Triangle Area: {area:.2f} square units")

triangleareafromcoordinates()