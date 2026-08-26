def triangletypebysides():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Sides must be positive.")
        return

    if (side1 + side2 <= side3 or
        side1 + side3 <= side2 or
        side2 + side3 <= side1):
        print("Invalid Triangle.")
        return

    if side1 == side2 == side3:
        print("Triangle Type: Equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Triangle Type: Isosceles")
    else:
        print("Triangle Type: Scalene")

triangletypebysides()