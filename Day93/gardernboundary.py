def gardenboundary():
    length = float(input("Enter garden length: "))
    width = float(input("Enter garden width: "))

    boundary = 2 * (length + width)

    print("Garden Boundary:", boundary)

gardenboundary()