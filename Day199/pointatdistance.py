def pointatdistance():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    d = float(input("Enter distance: "))

    length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    if length == 0:
        if d == 0:
            print("Point:", x1, y1)
        else:
            print("Invalid distance")
    elif 0 <= d <= length:
        x = x1 + d * (x2 - x1) / length
        y = y1 + d * (y2 - y1) / length
        print("Point:", x, y)
    else:
        print("Invalid distance")

pointatdistance()