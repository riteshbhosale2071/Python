import math

def distancebetweentwopoints():
    x1 = float(input("Enter the X-coordinate of the first point: "))
    y1 = float(input("Enter the Y-coordinate of the first point: "))

    x2 = float(input("Enter the X-coordinate of the second point: "))
    y2 = float(input("Enter the Y-coordinate of the second point: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"First Point: ({x1:.2f}, {y1:.2f})")
    print(f"Second Point: ({x2:.2f}, {y2:.2f})")
    print(f"Distance: {distance:.2f} units")

distancebetweentwopoints()