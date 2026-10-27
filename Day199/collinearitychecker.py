def collinearitychecker():
    print("Collinearity Checker")

    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))

    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if abs(area) < 0.000001:
        print("The three points are collinear.")
    else:
        print("The three points are not collinear.")

collinearitychecker()