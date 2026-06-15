def identify():
    sides = int(input("Enter number of sides: "))

    if sides == 3:
        print("Shape: Triangle")

    elif sides == 4:
        print("Shape: Quadrilateral")

    elif sides == 5:
        print("Shape: Pentagon")

    elif sides == 6:
        print("Shape: Hexagon")

    else:
        print("Shape Not Identified")

identify()