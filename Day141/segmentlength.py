import math

def segmentlength():
    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))

    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("Length of Line Segment:", length)

segmentlength()