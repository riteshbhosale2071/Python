def polygonside():
    sides = int(input("Enter the number of sides: "))

    if sides == 3:
        print("Polygon: Triangle")
    elif sides == 4:
        print("Polygon: Quadrilateral")
    elif sides == 5:
        print("Polygon: Pentagon")
    elif sides == 6:
        print("Polygon: Hexagon")
    elif sides == 7:
        print("Polygon: Heptagon")
    elif sides == 8:
        print("Polygon: Octagon")
    elif sides > 8:
        print("Polygon with", sides, "sides")
    else:
        print("A polygon must have at least 3 sides.")

polygonside()