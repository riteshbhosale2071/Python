import math

def congruentsegment():
    print("Enter endpoints of the first line segment.")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    print("\nEnter endpoints of the second line segment.")
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    x4 = float(input("Enter x4: "))
    y4 = float(input("Enter y4: "))

    length1 = math.hypot(x2 - x1, y2 - y1)
    length2 = math.hypot(x4 - x3, y4 - y3)

    print("\nFirst Segment Length:", length1)
    print("Second Segment Length:", length2)

    if math.isclose(length1, length2, rel_tol=1e-9):
        print("The line segments are Congruent.")
    else:
        print("The line segments are Not Congruent.")

congruentsegment()