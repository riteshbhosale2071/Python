import math

def trianglecircumcentrelogic():
    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    determinant = 2 * (
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )

    if math.isclose(determinant, 0):
        print("Circumcentre does not exist uniquely.")
        print("The three points are collinear.")
        return

    ux = (
        (x1**2 + y1**2) * (y2 - y3) +
        (x2**2 + y2**2) * (y3 - y1) +
        (x3**2 + y3**2) * (y1 - y2)
    ) / determinant

    uy = (
        (x1**2 + y1**2) * (x3 - x2) +
        (x2**2 + y2**2) * (x1 - x3) +
        (x3**2 + y3**2) * (x2 - x1)
    ) / determinant

    print("Circumcentre:", (ux, uy))

trianglecircumcentrelogic()