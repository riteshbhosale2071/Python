import math

def trianglecentre():
    print("Enter the coordinates of the three vertices.")

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    a = math.hypot(x2 - x3, y2 - y3)
    b = math.hypot(x1 - x3, y1 - y3)
    c = math.hypot(x1 - x2, y1 - y2)

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3

    perimeter = a + b + c
    incenter_x = (a * x1 + b * x2 + c * x3) / perimeter
    incenter_y = (a * y1 + b * y2 + c * y3) / perimeter

    determinant = 2 * (
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )

    if math.isclose(determinant, 0):
        print("The vertices are collinear.")
        return

    circumcenter_x = (
        (x1**2 + y1**2) * (y2 - y3) +
        (x2**2 + y2**2) * (y3 - y1) +
        (x3**2 + y3**2) * (y1 - y2)
    ) / determinant

    circumcenter_y = (
        (x1**2 + y1**2) * (x3 - x2) +
        (x2**2 + y2**2) * (x1 - x3) +
        (x3**2 + y3**2) * (x2 - x1)
    ) / determinant

    print("\n--- Triangle Centres ---")
    print("Centroid:", (centroid_x, centroid_y))
    print("Incentre:", (incenter_x, incenter_y))
    print("Circumcentre:", (circumcenter_x, circumcenter_y))

    orthocenter_x = x1 + x2 + x3 - 2 * circumcenter_x
    orthocenter_y = y1 + y2 + y3 - 2 * circumcenter_y

    print("Orthocentre:", (orthocenter_x, orthocenter_y))

trianglecentre()