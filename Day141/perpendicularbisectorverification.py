import math

def perpendicularbisectorverification():
    x1 = float(input("Enter x-coordinate of first endpoint: "))
    y1 = float(input("Enter y-coordinate of first endpoint: "))

    x2 = float(input("Enter x-coordinate of second endpoint: "))
    y2 = float(input("Enter y-coordinate of second endpoint: "))

    x = float(input("Enter x-coordinate of point to verify: "))
    y = float(input("Enter y-coordinate of point to verify: "))

    if x1 == x2 and y1 == y2:
        print("Invalid line segment. Endpoints must be different.")
        return

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    distance1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    distance2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)

    print("Midpoint:", (mid_x, mid_y))
    print("Distance from first endpoint:", distance1)
    print("Distance from second endpoint:", distance2)

    if math.isclose(distance1, distance2, rel_tol=1e-9):
        print("The point lies on the perpendicular bisector.")
    else:
        print("The point does not lie on the perpendicular bisector.")

perpendicularbisectorverification()