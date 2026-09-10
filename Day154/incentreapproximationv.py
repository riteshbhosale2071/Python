def incentreapproximation():
    print("Incentre Approximation Program :")

    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
        return

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    perimeter = a + b + c

    x = (a * x1 + b * x2 + c * x3) / perimeter
    y = (a * y1 + b * y2 + c * y3) / perimeter

    print("Approximate Incentre: ({:.2f}, {:.2f})".format(x, y))

incentreapproximation()