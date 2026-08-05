def kiteshape():
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))
    side4 = float(input("Enter the fourth side: "))

    if side1 == side2 and side3 == side4:
        print("The given sides form a Kite.")
    else:
        print("The given sides do not form a Kite.")

kiteshape()