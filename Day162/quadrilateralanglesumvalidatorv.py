def quadrilateralanglesumvalidator():
    print("Quadrilateral Angle-Sum Validator :")

    angle1 = float(input("Enter angle 1: "))
    angle2 = float(input("Enter angle 2: "))
    angle3 = float(input("Enter angle 3: "))
    angle4 = float(input("Enter angle 4: "))

    total = angle1 + angle2 + angle3 + angle4

    print("Sum of angles =", total)
    print("Required sum for a quadrilateral = 360 degrees")

    if total == 360:
        print("The angles form a valid quadrilateral.")
    else:
        print("The angles do not form a valid quadrilateral.")

quadrilateralanglesumvalidator()