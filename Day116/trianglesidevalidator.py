def triangle():
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))

    if (side1 + side2 > side3 and
        side1 + side3 > side2 and
        side2 + side3 > side1):
        print("The given sides form a valid triangle.")
    else:
        print("The given sides do not form a valid triangle.")

triangle()