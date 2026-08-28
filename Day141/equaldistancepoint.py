import math

def equaldistancepoint():
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))

    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    distance1 = math.sqrt(
        (midpoint_x - x1) ** 2 + (midpoint_y - y1) ** 2
    )

    distance2 = math.sqrt(
        (midpoint_x - x2) ** 2 + (midpoint_y - y2) ** 2
    )

    print("Equidistant Point (Midpoint):",
          (midpoint_x, midpoint_y))
    print("Distance from First Point:", distance1)
    print("Distance from Second Point:", distance2)

equaldistancepoint()