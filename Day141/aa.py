import math

def equidistantpoint():
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))

    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    x3 = float(input("Enter x-coordinate of point to check: "))
    y3 = float(input("Enter y-coordinate of point to check: "))

    distance1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    distance2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

    print("Distance from First Point:", distance1)
    print("Distance from Second Point:", distance2)

    if math.isclose(distance1, distance2, rel_tol=1e-9):
        print("The point is equidistant from both points.")
    else:
        print("The point is not equidistant from both points.")

equidistantpoint()