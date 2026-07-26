def planeobject():
    sides = int(input("Enter number of sides: "))

    if sides == 3:
        print("Triangle")
    elif sides == 4:
        print("Quadrilateral")
    elif sides == 5:
        print("Pentagon")
    elif sides == 6:
        print("Hexagon")
    else:
        print("Unknown Plane Object")

planeobject()