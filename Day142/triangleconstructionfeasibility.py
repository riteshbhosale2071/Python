def triangleconstructionfeasibility():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Construction is not possible.")
        print("All side lengths must be positive.")
        return

    sides = sorted([side1, side2, side3])

    if sides[0] + sides[1] > sides[2]:
        print("Triangle Construction is Possible.")
    else:
        print("Triangle Construction is Not Possible.")
        print("The sum of the two smaller sides must be greater than the largest side.")

triangleconstructionfeasibility()