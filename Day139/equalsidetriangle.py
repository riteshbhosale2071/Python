import math

def equalsidetriangle():
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("All sides must be positive.")
        return

    if not (side1 + side2 > side3 and
            side1 + side3 > side2 and
            side2 + side3 > side1):
        print("The given sides cannot form a triangle.")
        return

    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
        print("All three sides are equal.")
        print("Each angle is 60°.")
        print("Perimeter:", 3 * side1)
    else:
        print("The triangle is not Equilateral.")

equalsidetriangle()