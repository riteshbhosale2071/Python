def squarepropertyvalidator():
    print("Square Property Validator :")

    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    side4 = float(input("Enter side 4: "))

    angle1 = float(input("Enter angle 1: "))
    angle2 = float(input("Enter angle 2: "))
    angle3 = float(input("Enter angle 3: "))
    angle4 = float(input("Enter angle 4: "))

    if side1 == side2 and side2 == side3 and side3 == side4:
        if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
            print("All sides are equal.")
            print("All angles are 90 degrees.")
            print("The given shape satisfies the properties of a square.")
        else:
            print("All sides are equal, but all angles are not 90 degrees.")
            print("The shape is not a square.")
    else:
        print("All four sides are not equal.")
        print("The shape is not a square.")

squarepropertyvalidator()