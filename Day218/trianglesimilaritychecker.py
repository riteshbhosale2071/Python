def trianglesimilaritychecker():
    print("Triangle Similarity Checker")

    print("\nEnter sides of first triangle:")
    a1 = float(input("Enter first side: "))
    b1 = float(input("Enter second side: "))
    c1 = float(input("Enter third side: "))

    print("\nEnter sides of second triangle:")
    a2 = float(input("Enter first side: "))
    b2 = float(input("Enter second side: "))
    c2 = float(input("Enter third side: "))

    if min(a1, b1, c1, a2, b2, c2) <= 0:
        print("Side lengths must be positive.")
        return

    if a1 + b1 <= c1 or a1 + c1 <= b1 or b1 + c1 <= a1:
        print("First triangle is invalid.")
        return

    if a2 + b2 <= c2 or a2 + c2 <= b2 or b2 + c2 <= a2:
        print("Second triangle is invalid.")
        return

    triangle1 = sorted([a1, b1, c1])
    triangle2 = sorted([a2, b2, c2])

    ratio1 = triangle2[0] / triangle1[0]
    ratio2 = triangle2[1] / triangle1[1]
    ratio3 = triangle2[2] / triangle1[2]

    print("\nTriangle Similarity Analysis:")
    print("First Triangle Sides:", triangle1)
    print("Second Triangle Sides:", triangle2)

    if math.isclose(ratio1, ratio2, rel_tol=1e-9) and math.isclose(ratio2, ratio3, rel_tol=1e-9):
        print("Result: Triangles are Similar.")
        print("Similarity Ratio:", round(ratio1, 2))
    else:
        print("Result: Triangles are Not Similar.")

trianglesimilaritychecker()