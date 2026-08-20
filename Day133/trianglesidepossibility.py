def trianglesidepossibility():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Sides must be positive.")
        return

    if (side1 + side2 > side3 and
        side1 + side3 > side2 and
        side2 + side3 > side1):
        print("A triangle can be formed with these sides.")
    else:
        print("A triangle cannot be formed with these sides.")

trianglesidepossibility()