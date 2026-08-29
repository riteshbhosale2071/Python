import math

def perpendicularlinevalidator():
    print("Enter the coordinates of two points for Line 1.")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    print("\nEnter the coordinates of two points for Line 2.")
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    x4 = float(input("Enter x4: "))
    y4 = float(input("Enter y4: "))

    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    if dx1 == 0 and dy1 == 0 or dx2 == 0 and dy2 == 0:
        print("Invalid line: endpoints must be different.")
        return

    dot_product = dx1 * dx2 + dy1 * dy2

    if math.isclose(dot_product, 0, abs_tol=1e-9):
        print("The two lines are Perpendicular.")
    else:
        print("The two lines are Not Perpendicular.")

perpendicularlinevalidator()