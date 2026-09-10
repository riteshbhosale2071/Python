def circumcentrecoordinatefinder():
    print("Circumcentre Coordinate Finder :")

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    if d == 0:
        print("The points are collinear.")
        print("Circumcentre cannot be determined.")
        return

    x = ((x1 * x1 + y1 * y1) * (y2 - y3) +
         (x2 * x2 + y2 * y2) * (y3 - y1) +
         (x3 * x3 + y3 * y3) * (y1 - y2)) / d

    y = ((x1 * x1 + y1 * y1) * (x3 - x2) +
         (x2 * x2 + y2 * y2) * (x1 - x3) +
         (x3 * x3 + y3 * y3) * (x2 - x1)) / d

    print("Circumcentre: ({:.2f}, {:.2f})".format(x, y))

circumcentrecoordinatefinder()