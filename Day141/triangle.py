import math

def triangleincentreconcept():
    print("Enter the coordinates of the three vertices.")

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    a = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if a + b <= c or a + c <= b or b + c <= a:
        print("The given points do not form a valid triangle.")
        return

    perimeter = a + b + c

    incenter_x = (a * x1 + b * x2 + c * x3) / perimeter
    incenter_y = (a * y1 + b * y2 + c * y3) / perimeter

    print("\nTriangle Side Lengths:")
    print("a =", a)
    print("b =", b)
    print("c =", c)

    print("\nIncentre:", (incenter_x, incenter_y))
    print("The Incentre is the point where the three angle bisectors meet.")

triangleincentreconcept()