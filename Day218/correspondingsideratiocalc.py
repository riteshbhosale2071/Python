def correspondingsideratiocalc():
    print("Corresponding Side Ratio Calculator")

    print("\nEnter the corresponding sides of Triangle 1:")
    a1 = float(input("Enter first side: "))
    b1 = float(input("Enter second side: "))
    c1 = float(input("Enter third side: "))

    print("\nEnter the corresponding sides of Triangle 2:")
    a2 = float(input("Enter first side: "))
    b2 = float(input("Enter second side: "))
    c2 = float(input("Enter third side: "))

    if min(a1, b1, c1, a2, b2, c2) <= 0:
        print("All side lengths must be positive.")
        return

    ratio1 = a1 / a2
    ratio2 = b1 / b2
    ratio3 = c1 / c2

    print("\nCorresponding Side Ratios:")
    print("First ratio:", round(ratio1, 4))
    print("Second ratio:", round(ratio2, 4))
    print("Third ratio:", round(ratio3, 4))

    if abs(ratio1 - ratio2) < 1e-9 and abs(ratio2 - ratio3) < 1e-9:
        print("\nAll corresponding sides are proportional.")
        print("The triangles satisfy the SSS similarity condition.")
        print("Scale factor:", round(ratio1, 4))
    else:
        print("\nCorresponding sides are not proportional.")
        print("The triangles do not satisfy the SSS similarity condition.")

correspondingsideratiocalc()