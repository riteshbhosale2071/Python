def collinearpoint():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    x3 = int(input("Enter x3: "))
    y3 = int(input("Enter y3: "))

    if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
        print("Points are Collinear")
    else:
        print("Points are Not Collinear")

collinearpoint()