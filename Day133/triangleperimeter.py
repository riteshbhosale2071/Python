def triangleperimeter():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("All sides must be positive.")
        return

    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("The given sides cannot form a triangle.")
        return

    perimeter = side1 + side2 + side3

    print("Perimeter of the Triangle:", perimeter)

triangleperimeter()