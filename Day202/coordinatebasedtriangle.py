import math

def coordinatebasedtriangle():
    x1 = float(input("Enter x-coordinate of first vertex: "))
    y1 = float(input("Enter y-coordinate of first vertex: "))

    x2 = float(input("Enter x-coordinate of second vertex: "))
    y2 = float(input("Enter y-coordinate of second vertex: "))

    x3 = float(input("Enter x-coordinate of third vertex: "))
    y3 = float(input("Enter y-coordinate of third vertex: "))

    area = abs(
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    ) / 2

    if area == 0:
        print("Invalid triangle. The points are collinear or identical.")
        return

    side_a = math.dist((x1, y1), (x2, y2))
    side_b = math.dist((x2, y2), (x3, y3))
    side_c = math.dist((x3, y3), (x1, y1))

    perimeter = side_a + side_b + side_c

    print("Triangle constructed successfully.")
    print(f"Side 1: {side_a:.2f}")
    print(f"Side 2: {side_b:.2f}")
    print(f"Side 3: {side_c:.2f}")
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")

coordinatebasedtriangle()