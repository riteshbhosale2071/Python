def trianglecentrevisualdata():
    print("Triangle Centre Visual Data Generator :")

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if area == 0:
        print("Invalid triangle.")
        return

    side_a = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    side_b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    side_c = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3

    perimeter = side_a + side_b + side_c

    incentre_x = (side_a * x1 + side_b * x2 + side_c * x3) / perimeter
    incentre_y = (side_a * y1 + side_b * y2 + side_c * y3) / perimeter

    print("\nTriangle Data :")
    print("Vertex A: ({:.2f}, {:.2f})".format(x1, y1))
    print("Vertex B: ({:.2f}, {:.2f})".format(x2, y2))
    print("Vertex C: ({:.2f}, {:.2f})".format(x3, y3))

    print("\nSide Lengths :")
    print("Side a: {:.2f}".format(side_a))
    print("Side b: {:.2f}".format(side_b))
    print("Side c: {:.2f}".format(side_c))

    print("\nCentre Data :")
    print("Centroid: ({:.2f}, {:.2f})".format(centroid_x, centroid_y))
    print("Incentre: ({:.2f}, {:.2f})".format(incentre_x, incentre_y))

    print("\nVisual Representation :")
    print("A ({:.1f}, {:.1f})".format(x1, y1))
    print("       \\")
    print("        \\")
    print("         CEN")
    print("        /  \\")
    print("       /    \\")
    print("B ({:.1f}, {:.1f}) ---- C ({:.1f}, {:.1f})".format(
        x2, y2, x3, y3
    ))

    print("\nCentroid is marked as CEN.")
    print("Incentre coordinates are provided for plotting.")

trianglecentrevisualdata()